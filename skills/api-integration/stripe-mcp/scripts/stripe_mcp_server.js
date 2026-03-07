#!/usr/bin/env node
"""
Stripe MCP Server
Model Context Protocol server for Stripe integration
"""

const { Server } = require('@modelcontextprotocol/sdk/server/index.js');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio.js');
const stripe = require('stripe');
require('dotenv').config();

// Initialize Stripe with API key
const stripeClient = stripe(process.env.STRIPE_API_KEY);

// Create MCP server
const server = new Server(
  {
    name: 'stripe-mcp',
    version: '1.0.0',
  },
  {
    capabilities: {
      resources: {},
      tools: {},
    },
  }
);

// Tool: Create payment intent
server.setRequestHandler('tools/call', async (request) => {
  const { name, arguments: args } = request.params;
  
  switch (name) {
    case 'create_payment_intent': {
      try {
        const paymentIntent = await stripeClient.paymentIntents.create({
          amount: args.amount,
          currency: args.currency || 'usd',
          payment_method_types: ['card'],
          metadata: args.metadata || {},
        });
        
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify({
                success: true,
                client_secret: paymentIntent.client_secret,
                payment_intent_id: paymentIntent.id,
                amount: paymentIntent.amount,
                currency: paymentIntent.currency,
                status: paymentIntent.status,
              }, null, 2),
            },
          ],
        };
      } catch (error) {
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify({
                success: false,
                error: error.message,
              }, null, 2),
            },
          ],
        };
      }
    }
    
    case 'create_customer': {
      try {
        const customer = await stripeClient.customers.create({
          email: args.email,
          name: args.name,
          phone: args.phone,
          metadata: args.metadata || {},
        });
        
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify({
                success: true,
                customer_id: customer.id,
                email: customer.email,
                name: customer.name,
                created: customer.created,
              }, null, 2),
            },
          ],
        };
      } catch (error) {
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify({
                success: false,
                error: error.message,
              }, null, 2),
            },
          ],
        };
      }
    }
    
    case 'create_subscription': {
      try {
        const subscription = await stripeClient.subscriptions.create({
          customer: args.customer_id,
          items: [
            {
              price: args.price_id,
            },
          ],
          metadata: args.metadata || {},
        });
        
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify({
                success: true,
                subscription_id: subscription.id,
                customer_id: subscription.customer,
                status: subscription.status,
                current_period_start: subscription.current_period_start,
                current_period_end: subscription.current_period_end,
              }, null, 2),
            },
          ],
        };
      } catch (error) {
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify({
                success: false,
                error: error.message,
              }, null, 2),
            },
          ],
        };
      }
    }
    
    case 'list_invoices': {
      try {
        const invoices = await stripeClient.invoices.list({
          limit: args.limit || 10,
          customer: args.customer_id,
        });
        
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify({
                success: true,
                count: invoices.data.length,
                invoices: invoices.data.map(invoice => ({
                  id: invoice.id,
                  customer: invoice.customer,
                  amount_paid: invoice.amount_paid,
                  status: invoice.status,
                  created: invoice.created,
                  pdf_url: invoice.invoice_pdf,
                })),
              }, null, 2),
            },
          ],
        };
      } catch (error) {
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify({
                success: false,
                error: error.message,
              }, null, 2),
            },
          ],
        };
      }
    }
    
    default:
      return {
        content: [
          {
            type: 'text',
            text: `Unknown tool: ${name}`,
          },
        ],
      };
  }
});

// Start server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('Stripe MCP server running on stdio');
}

main().catch((error) => {
  console.error('Server error:', error);
  process.exit(1);
});
