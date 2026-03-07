#!/usr/bin/env python3
"""
Shopify Order Processing Script
Handles order management operations
"""
import os
import sys
import json
import argparse
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

class ShopifyOrders:
    def __init__(self):
        self.api_key = os.getenv('SHOPIFY_API_KEY')
        self.password = os.getenv('SHOPIFY_PASSWORD')
        self.store_name = os.getenv('SHOPIFY_STORE_NAME')
        self.api_version = os.getenv('SHOPIFY_API_VERSION', '2024-01')
        
        if not all([self.api_key, self.password, self.store_name]):
            raise ValueError("Missing Shopify API credentials in .env file")
        
        self.base_url = f"https://{self.api_key}:{self.password}@{self.store_name}.myshopify.com/admin/api/{self.api_version}"
    
    def list_orders(self, status=None, limit=50, created_at_min=None):
        """List orders with optional filters"""
        url = f"{self.base_url}/orders.json"
        params = {'limit': limit}
        
        if status:
            params['status'] = status
        if created_at_min:
            params['created_at_min'] = created_at_min
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_order(self, order_id):
        """Get specific order by ID"""
        url = f"{self.base_url}/orders/{order_id}.json"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    def create_order(self, order_data):
        """Create new order"""
        url = f"{self.base_url}/orders.json"
        payload = {"order": order_data}
        
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    
    def update_order(self, order_id, order_data):
        """Update existing order"""
        url = f"{self.base_url}/orders/{order_id}.json"
        payload = {"order": order_data}
        
        response = requests.put(url, json=payload)
        response.raise_for_status()
        return response.json()
    
    def cancel_order(self, order_id):
        """Cancel an order"""
        url = f"{self.base_url}/orders/{order_id}/cancel.json"
        response = requests.post(url)
        response.raise_for_status()
        return response.json()
    
    def fulfill_order(self, order_id, fulfillment_data):
        """Fulfill an order"""
        url = f"{self.base_url}/orders/{order_id}/fulfillments.json"
        payload = {"fulfillment": fulfillment_data}
        
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    
    def generate_sales_report(self, days=30):
        """Generate sales report for specified period"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # Get orders from the period
        orders = self.list_orders(
            status='any',
            limit=250,
            created_at_min=start_date.isoformat()
        )
        
        report = {
            'period': {
                'start': start_date.isoformat(),
                'end': end_date.isoformat(),
                'days': days
            },
            'total_orders': len(orders.get('orders', [])),
            'total_revenue': 0,
            'average_order_value': 0,
            'orders_by_status': {},
            'top_products': {}
        }
        
        # Calculate metrics
        for order in orders.get('orders', []):
            report['total_revenue'] += float(order.get('total_price', 0))
            
            status = order.get('financial_status', 'unknown')
            report['orders_by_status'][status] = report['orders_by_status'].get(status, 0) + 1
            
            # Track products
            for item in order.get('line_items', []):
                product_id = item.get('product_id')
                if product_id:
                    report['top_products'][product_id] = report['top_products'].get(product_id, 0) + item.get('quantity', 0)
        
        if report['total_orders'] > 0:
            report['average_order_value'] = report['total_revenue'] / report['total_orders']
        
        # Sort top products
        report['top_products'] = dict(sorted(
            report['top_products'].items(),
            key=lambda x: x[1],
            reverse=True
        )[:10])
        
        return report

def main():
    parser = argparse.ArgumentParser(description='Manage Shopify orders')
    parser.add_argument('--action', required=True, 
                       choices=['list', 'get', 'create', 'update', 'cancel', 'fulfill', 'report'],
                       help='Action to perform')
    parser.add_argument('--id', help='Order ID (for get, update, cancel, fulfill)')
    parser.add_argument('--data', help='JSON data for create/update/fulfill actions')
    parser.add_argument('--status', help='Order status filter for list action')
    parser.add_argument('--limit', type=int, default=50, help='Limit for list action')
    parser.add_argument('--days', type=int, default=30, help='Days for sales report')
    
    args = parser.parse_args()
    
    try:
        shopify = ShopifyOrders()
        
        if args.action == 'list':
            result = shopify.list_orders(status=args.status, limit=args.limit)
        elif args.action == 'get':
            if not args.id:
                raise ValueError("Order ID required for get action")
            result = shopify.get_order(args.id)
        elif args.action == 'create':
            if not args.data:
                raise ValueError("Order data required for create action")
            order_data = json.loads(args.data)
            result = shopify.create_order(order_data)
        elif args.action == 'update':
            if not args.id or not args.data:
                raise ValueError("Order ID and data required for update action")
            order_data = json.loads(args.data)
            result = shopify.update_order(args.id, order_data)
        elif args.action == 'cancel':
            if not args.id:
                raise ValueError("Order ID required for cancel action")
            result = shopify.cancel_order(args.id)
        elif args.action == 'fulfill':
            if not args.id or not args.data:
                raise ValueError("Order ID and fulfillment data required for fulfill action")
            fulfillment_data = json.loads(args.data)
            result = shopify.fulfill_order(args.id, fulfillment_data)
        elif args.action == 'report':
            result = shopify.generate_sales_report(days=args.days)
        
        print(json.dumps(result, indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
