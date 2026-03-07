#!/usr/bin/env python3
"""
Stripe Subscription Management Script
Handles subscription plans, pricing, and customer subscriptions
"""

import os
import stripe
from dotenv import load_dotenv
import json
from typing import Dict, Any, Optional, List

# Load environment variables
load_dotenv()

# Initialize Stripe
stripe.api_key = os.getenv('STRIPE_API_KEY')


def create_product(name: str, description: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a new product in Stripe
    """
    try:
        product_data = {'name': name}
        if description:
            product_data['description'] = description
        
        product = stripe.Product.create(**product_data)
        
        return {
            'success': True,
            'product_id': product.id,
            'name': product.name,
            'description': product.description,
            'created': product.created
        }
    except stripe.error.StripeError as e:
        return {
            'success': False,
            'error': str(e),
            'error_type': type(e).__name__
        }


def create_price(product_id: str, amount: int, currency: str = 'usd', 
                interval: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a price for a product
    
    Args:
        product_id: Stripe product ID
        amount: Price amount in smallest currency unit
        currency: Currency code
        interval: Billing interval ('month', 'year', etc.) or None for one-time
    """
    try:
        price_data = {
            'product': product_id,
            'unit_amount': amount,
            'currency': currency,
        }
        
        if interval:
            price_data['recurring'] = {'interval': interval}
        
        price = stripe.Price.create(**price_data)
        
        return {
            'success': True,
            'price_id': price.id,
            'product_id': price.product,
            'amount': price.unit_amount,
            'currency': price.currency,
            'type': price.type
        }
    except stripe.error.StripeError as e:
        return {
            'success': False,
            'error': str(e),
            'error_type': type(e).__name__
        }


def create_subscription(customer_id: str, price_id: str, 
                      metadata: Optional[Dict] = None) -> Dict[str, Any]:
    """
    Create a subscription for a customer
    """
    try:
        subscription_data = {
            'customer': customer_id,
            'items': [{'price': price_id}]
        }
        
        if metadata:
            subscription_data['metadata'] = metadata
        
        subscription = stripe.Subscription.create(**subscription_data)
        
        return {
            'success': True,
            'subscription_id': subscription.id,
            'customer_id': subscription.customer,
            'status': subscription.status,
            'current_period_start': subscription.current_period_start,
            'current_period_end': subscription.current_period_end,
            'items': [
                {
                    'price_id': item.price.id,
                    'quantity': item.quantity
                }
                for item in subscription.items.data
            ]
        }
    except stripe.error.StripeError as e:
        return {
            'success': False,
            'error': str(e),
            'error_type': type(e).__name__
        }


def cancel_subscription(subscription_id: str, 
                      cancel_at_period_end: bool = False) -> Dict[str, Any]:
    """
    Cancel a subscription
    """
    try:
        if cancel_at_period_end:
            subscription = stripe.Subscription.modify(
                subscription_id,
                cancel_at_period_end=True
            )
        else:
            subscription = stripe.Subscription.delete(subscription_id)
        
        return {
            'success': True,
            'subscription_id': subscription.id,
            'status': subscription.status,
            'cancel_at_period_end': getattr(subscription, 'cancel_at_period_end', False),
            'canceled_at': getattr(subscription, 'canceled_at', None)
        }
    except stripe.error.StripeError as e:
        return {
            'success': False,
            'error': str(e),
            'error_type': type(e).__name__
        }


if __name__ == '__main__':
    # Example usage
    print("Stripe Subscription Management Script")
    print("=" * 40)
    
    # Test product creation
    print("\n1. Creating test product...")
    product_result = create_product(
        name="Premium Plan",
        description="Access to premium features"
    )
    print(json.dumps(product_result, indent=2))
    
    if product_result['success']:
        # Test price creation
        print("\n2. Creating monthly price...")
        price_result = create_price(
            product_id=product_result['product_id'],
            amount=2999,  # $29.99
            currency='usd',
            interval='month'
        )
        print(json.dumps(price_result, indent=2))
