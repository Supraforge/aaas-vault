---
name: shopify-mcp
description: Integrates with Shopify API for e-commerce automation, store management, product catalog, and order processing
version: 1.0.0
dependencies: ["python3", "node", "npm"]
inputs:
  - name: shopify_api_key
    description: Shopify Admin API access token
  - name: shopify_password
    description: Shopify Admin API password (if using private app)
  - name: shopify_store_name
    description: Shopify store name (xxxx.myshopify.com)
  - name: shopify_api_version
    description: Shopify API version (default: 2024-01)
outputs:
  - type: stdout
    description: JSON response from Shopify API
  - type: file
    description: Exported product catalog, order reports, or analytics data
---

# Shopify MCP Skill

## 🎯 Triggers
- "Connect to my Shopify store and list products"
- "Create a new product in Shopify"
- "Process recent orders and generate report"
- "Update inventory levels"
- "Analyze store performance metrics"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/shopify-mcp/test.sh`.
- [ ] Check `.env` contains required Shopify API credentials.
- [ ] Ensure Node.js and Python are installed.

## 📋 Workflow
1. **Authentication**: Connect to Shopify Admin API using store credentials
2. **Resource Selection**: Choose operation (products, orders, customers, inventory)
3. **Data Processing**: Transform and validate data for Shopify API
4. **API Execution**: Make authenticated requests to Shopify endpoints
5. **Response Handling**: Process and format API responses

## 🛠️ Script Reference
- Use `scripts/shopify_mcp_server.js` for Node.js MCP server
- Use `scripts/shopify_products.py` for product management operations
- Use `scripts/shopify_orders.py` for order processing
- Use `scripts/shopify_analytics.py` for store analytics

## 🔌 API Endpoints Covered
- Products: CRUD operations, inventory management
- Orders: List, create, update, fulfill orders
- Customers: Customer management and segmentation
- Inventory: Stock levels, locations, adjustments
- Analytics: Sales reports, traffic data, conversion rates
- Webhooks: Event subscription and management

## 📊 Example Usage
```bash
# List all products
python3 scripts/shopify_products.py --action list --limit 10

# Create new product
python3 scripts/shopify_products.py --action create --data '{"title":"New Product","price":"29.99"}'

# Get recent orders
python3 scripts/shopify_orders.py --action list --status open
```
