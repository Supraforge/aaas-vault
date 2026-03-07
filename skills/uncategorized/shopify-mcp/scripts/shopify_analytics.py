#!/usr/bin/env python3
"""
Shopify Analytics Script
Provides store analytics and performance metrics
"""
import os
import sys
import json
import argparse
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# Note: Shopify Analytics API requires Shopify Plus or specific permissions
# This script uses the REST API where possible and provides calculated metrics

class ShopifyAnalytics:
    def __init__(self):
        self.api_key = os.getenv('SHOPIFY_API_KEY')
        self.password = os.getenv('SHOPIFY_PASSWORD')
        self.store_name = os.getenv('SHOPIFY_STORE_NAME')
        self.api_version = os.getenv('SHOPIFY_API_VERSION', '2024-01')
        
        if not all([self.api_key, self.password, self.store_name]):
            raise ValueError("Missing Shopify API credentials in .env file")
        
        self.base_url = f"https://{self.api_key}:{self.password}@{self.store_name}.myshopify.com/admin/api/{self.api_version}"
    
    def get_store_metrics(self, days=30):
        """Calculate basic store metrics from order data"""
        import requests
        
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # Get orders for the period
        url = f"{self.base_url}/orders.json"
        params = {
            'limit': 250,
            'status': 'any',
            'created_at_min': start_date.isoformat()
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        orders = response.json().get('orders', [])
        
        metrics = {
            'period': {
                'start': start_date.isoformat(),
                'end': end_date.isoformat(),
                'days': days
            },
            'total_orders': len(orders),
            'total_revenue': 0,
            'revenue_by_status': {},
            'customer_count': len(set(order.get('customer', {}).get('id') for order in orders if order.get('customer'))),
            'average_order_value': 0,
            'conversion_rate': 0,  # Would need session data from Analytics API
            'top_customers': [],
            'sales_trend': {}
        }
        
        # Calculate revenue and group by status
        customer_spend = {}
        daily_sales = {}
        
        for order in orders:
            order_value = float(order.get('total_price', 0))
            metrics['total_revenue'] += order_value
            
            # Revenue by status
            status = order.get('financial_status', 'unknown')
            metrics['revenue_by_status'][status] = metrics['revenue_by_status'].get(status, 0) + order_value
            
            # Customer spending
            customer_id = order.get('customer', {}).get('id')
            if customer_id:
                customer_spend[customer_id] = customer_spend.get(customer_id, 0) + order_value
            
            # Daily sales trend
            created_date = order.get('created_at', '').split('T')[0]
            if created_date:
                daily_sales[created_date] = daily_sales.get(created_date, 0) + order_value
        
        # Calculate averages
        if metrics['total_orders'] > 0:
            metrics['average_order_value'] = metrics['total_revenue'] / metrics['total_orders']
        
        # Top customers
        top_customers = sorted(customer_spend.items(), key=lambda x: x[1], reverse=True)[:10]
        metrics['top_customers'] = [
            {'customer_id': cust_id, 'total_spent': spend}
            for cust_id, spend in top_customers
        ]
        
        # Sales trend (last 7 days)
        for i in range(7):
            date = (end_date - timedelta(days=i)).strftime('%Y-%m-%d')
            metrics['sales_trend'][date] = daily_sales.get(date, 0)
        
        return metrics
    
    def get_product_performance(self, limit=20):
        """Get product performance metrics"""
        import requests
        
        # Get products with their variants
        url = f"{self.base_url}/products.json"
        params = {
            'limit': limit,
            'fields': 'id,title,variants,images'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        products = response.json().get('products', [])
        
        # Get recent orders to calculate sales
        orders_url = f"{self.base_url}/orders.json"
        orders_params = {'limit': 100, 'status': 'any'}
        orders_response = requests.get(orders_url, params=orders_params)
        orders_response.raise_for_status()
        orders = orders_response.json().get('orders', [])
        
        # Calculate product sales
        product_sales = {}
        for order in orders:
            for item in order.get('line_items', []):
                product_id = item.get('product_id')
                if product_id:
                    product_sales[product_id] = product_sales.get(product_id, 0) + item.get('quantity', 0)
        
        # Enrich products with sales data
        performance_data = []
        for product in products:
            product_id = product.get('id')
            variants = product.get('variants', [])
            
            total_inventory = sum(variant.get('inventory_quantity', 0) for variant in variants)
            total_sold = product_sales.get(product_id, 0)
            
            performance_data.append({
                'id': product_id,
                'title': product.get('title'),
                'total_sold': total_sold,
                'inventory': total_inventory,
                'variants_count': len(variants),
                'has_images': len(product.get('images', [])) > 0,
                'sell_through_rate': (total_sold / (total_sold + total_inventory)) * 100 if (total_sold + total_inventory) > 0 else 0
            })
        
        # Sort by sales
        performance_data.sort(key=lambda x: x['total_sold'], reverse=True)
        
        return {
            'products_analyzed': len(performance_data),
            'top_performers': performance_data[:10],
            'low_inventory': [p for p in performance_data if p['inventory'] < 10],
            'summary': {
                'total_products': len(performance_data),
                'total_sold': sum(p['total_sold'] for p in performance_data),
                'average_sell_through': sum(p['sell_through_rate'] for p in performance_data) / len(performance_data) if performance_data else 0
            }
        }

def main():
    parser = argparse.ArgumentParser(description='Shopify Analytics')
    parser.add_argument('--action', required=True, choices=['metrics', 'products'],
                       help='Analytics action to perform')
    parser.add_argument('--days', type=int, default=30, help='Days for metrics analysis')
    parser.add_argument('--limit', type=int, default=20, help='Limit for product analysis')
    
    args = parser.parse_args()
    
    try:
        analytics = ShopifyAnalytics()
        
        if args.action == 'metrics':
            result = analytics.get_store_metrics(days=args.days)
        elif args.action == 'products':
            result = analytics.get_product_performance(limit=args.limit)
        
        print(json.dumps(result, indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
