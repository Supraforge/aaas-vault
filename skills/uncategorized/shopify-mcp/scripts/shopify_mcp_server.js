const { Server } = require('@modelcontextprotocol/sdk/server/index.js');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio.js');
const axios = require('axios');
require('dotenv').config();

class ShopifyMCPServer {
  constructor() {
    this.server = new Server(
      {
        name: 'shopify-mcp',
        version: '1.0.0',
      },
      {
        capabilities: {
          resources: {},
          tools: {},
        },
      }
    );

    this.setupHandlers();
    this.shopifyConfig = {
      apiKey: process.env.SHOPIFY_API_KEY,
      password: process.env.SHOPIFY_PASSWORD,
      storeName: process.env.SHOPIFY_STORE_NAME,
      apiVersion: process.env.SHOPIFY_API_VERSION || '2024-01',
    };
  }

  setupHandlers() {
    this.server.setRequestHandler('tools/list', async () => {
      return {
        tools: [
          {
            name: 'shopify_list_products',
            description: 'List products from Shopify store',
            inputSchema: {
              type: 'object',
              properties: {
                limit: { type: 'number', description: 'Number of products to return', default: 50 },
                fields: { type: 'string', description: 'Fields to include in response' },
              },
            },
          },
          {
            name: 'shopify_get_product',
            description: 'Get specific product by ID',
            inputSchema: {
              type: 'object',
              properties: {
                productId: { type: 'string', description: 'Shopify product ID', required: true },
              },
            },
          },
          {
            name: 'shopify_create_product',
            description: 'Create new product in Shopify',
            inputSchema: {
              type: 'object',
              properties: {
                productData: { type: 'object', description: 'Product data JSON', required: true },
              },
            },
          },
          {
            name: 'shopify_update_inventory',
            description: 'Update inventory levels',
            inputSchema: {
              type: 'object',
              properties: {
                inventoryItemId: { type: 'string', description: 'Inventory item ID', required: true },
                locationId: { type: 'string', description: 'Location ID', required: true },
                quantity: { type: 'number', description: 'New quantity', required: true },
              },
            },
          },
        ],
      };
    });

    this.server.setRequestHandler('tools/call', async (request) => {
      const { name, arguments: args } = request.params;
      
      try {
        switch (name) {
          case 'shopify_list_products':
            return await this.listProducts(args);
          case 'shopify_get_product':
            return await this.getProduct(args);
          case 'shopify_create_product':
            return await this.createProduct(args);
          case 'shopify_update_inventory':
            return await this.updateInventory(args);
          default:
            throw new Error(`Unknown tool: ${name}`);
        }
      } catch (error) {
        return {
          content: [
            {
              type: 'text',
              text: `Error: ${error.message}`,
            },
          ],
          isError: true,
        };
      }
    });
  }

  async makeShopifyRequest(endpoint, method = 'GET', data = null) {
    const { apiKey, password, storeName, apiVersion } = this.shopifyConfig;
    const url = `https://${apiKey}:${password}@${storeName}.myshopify.com/admin/api/${apiVersion}/${endpoint}`;
    
    const config = {
      method,
      url,
      headers: {
        'Content-Type': 'application/json',
      },
    };
    
    if (data) {
      config.data = data;
    }
    
    const response = await axios(config);
    return response.data;
  }

  async listProducts({ limit = 50, fields }) {
    const params = new URLSearchParams();
    params.append('limit', limit);
    if (fields) params.append('fields', fields);
    
    const data = await this.makeShopifyRequest(`products.json?${params.toString()}`);
    
    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify(data, null, 2),
        },
      ],
    };
  }

  async getProduct({ productId }) {
    const data = await this.makeShopifyRequest(`products/${productId}.json`);
    
    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify(data, null, 2),
        },
      ],
    };
  }

  async createProduct({ productData }) {
    const data = await this.makeShopifyRequest('products.json', 'POST', {
      product: productData,
    });
    
    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify(data, null, 2),
        },
      ],
    };
  }

  async updateInventory({ inventoryItemId, locationId, quantity }) {
    const data = await this.makeShopifyRequest('inventory_levels/set.json', 'POST', {
      location_id: locationId,
      inventory_item_id: inventoryItemId,
      available: quantity,
    });
    
    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify(data, null, 2),
        },
      ],
    };
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('Shopify MCP server running on stdio');
  }
}

const server = new ShopifyMCPServer();
server.run().catch(console.error);
