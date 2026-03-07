#!/usr/bin/env python3
"""
Shopify Product Management Script
Handles CRUD operations for Shopify products
"""
import os
import sys
import json
import argparse
import requests
from dotenv import load_dotenv

load_dotenv()

class ShopifyProducts:
    def __init__(self):
        self.api_key = os.getenv('SHOPIFY_API_KEY')
        self.password = os.getenv('SHOPIFY_PASSWORD')
        self.store_name = os.getenv('SHOPIFY_STORE_NAME')
        self.api_version = os.getenv('SHOPIFY_API_VERSION', '2024-01')
        
        if not all([self.api_key, self.password, self.store_name]):
            raise ValueError("Missing Shopify API credentials in .env file")
        
        self.base_url = f"https://{self.api_key}:{self.password}@{self.store_name}.myshopify.com/admin/api/{self.api_version}"
    
    def list_products(self, limit=50, fields=None):
        """List products from Shopify store"""
        url = f"{self.base_url}/products.json"
        params = {
            'limit': limit,
            'fields': fields if fields else 'id,title,variants,images'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_product(self, product_id):
        """Get specific product by ID"""
        url = f"{self.base_url}/products/{product_id}.json"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    def create_product(self, product_data):
        """Create new product in Shopify"""
        url = f"{self.base_url}/products.json"
        payload = {"product": product_data}
        
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    
    def update_product(self, product_id, product_data):
        """Update existing product"""
        url = f"{self.base_url}/products/{product_id}.json"
        payload = {"product": product_data}
        
        response = requests.put(url, json=payload)
        response.raise_for_status()
        return response.json()
    
    def delete_product(self, product_id):
        """Delete product from Shopify"""
        url = f"{self.base_url}/products/{product_id}.json"
        response = requests.delete(url)
        response.raise_for_status()
        return {"status": "success", "message": f"Product {product_id} deleted"}
    
    def update_inventory(self, inventory_item_id, location_id, quantity):
        """Update inventory level for a product"""
        url = f"{self.base_url}/inventory_levels/set.json"
        payload = {
            "location_id": location_id,
            "inventory_item_id": inventory_item_id,
            "available": quantity
        }
        
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

def main():
    parser = argparse.ArgumentParser(description='Manage Shopify products')
    parser.add_argument('--action', required=True, choices=['list', 'get', 'create', 'update', 'delete', 'inventory'],
                       help='Action to perform')
    parser.add_argument('--id', help='Product ID (for get, update, delete)')
    parser.add_argument('--data', help='JSON data for create/update actions')
    parser.add_argument('--limit', type=int, default=50, help='Limit for list action')
    parser.add_argument('--fields', help='Fields to include in response')
    parser.add_argument('--inventory-item', help='Inventory item ID for inventory action')
    parser.add_argument('--location', help='Location ID for inventory action')
    parser.add_argument('--quantity', type=int, help='Quantity for inventory action')
    
    args = parser.parse_args()
    
    try:
        shopify = ShopifyProducts()
        
        if args.action == 'list':
            result = shopify.list_products(limit=args.limit, fields=args.fields)
        elif args.action == 'get':
            if not args.id:
                raise ValueError("Product ID required for get action")
            result = shopify.get_product(args.id)
        elif args.action == 'create':
            if not args.data:
                raise ValueError("Product data required for create action")
            product_data = json.loads(args.data)
            result = shopify.create_product(product_data)
        elif args.action == 'update':
            if not args.id or not args.data:
                raise ValueError("Product ID and data required for update action")
            product_data = json.loads(args.data)
            result = shopify.update_product(args.id, product_data)
        elif args.action == 'delete':
            if not args.id:
                raise ValueError("Product ID required for delete action")
            result = shopify.delete_product(args.id)
        elif args.action == 'inventory':
            if not all([args.inventory_item, args.location, args.quantity is not None]):
                raise ValueError("Inventory item, location, and quantity required for inventory action")
            result = shopify.update_inventory(args.inventory_item, args.location, args.quantity)
        
        print(json.dumps(result, indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
