#!/usr/bin/env python3
"""
Stripe Payment Processing Script
Handles payment intents, charges, and refunds
"""

import os
import stripe
from dotenv import load_dotenv
import json
from typing import Dict, Any, Optional

# Load environment variables
load_dotenv()

# Initialize Stripe
stripe.api_key = os.getenv('STRIPE_API_KEY')


def create_payment_intent(amount: int, currency: str = 'usd', 
                         customer_id: Optional[str] = None, 
                         metadata: Optional[Dict] = None) -> Dict[str, Any]:
    """
    Create a payment intent for processing payments
    
    Args:
        amount: Amount in smallest currency unit (e.g., cents)
        currency: Currency code (default: 'usd')
        customer_id: Optional Stripe customer ID
        metadata: Optional metadata for the payment
    
    Returns:
        Payment intent object
    """
    try:
        intent_data = {
            'amount': amount,
            'currency': currency,
            'payment_method_types': ['card'],
            'automatic_payment_methods': {
                'enabled': True,
                'allow_redirects': 'never'
            }
        }
        
        if customer_id:
            intent_data['customer'] = customer_id
        
        if metadata:
            intent_data['metadata'] = metadata
        
        payment_intent = stripe.PaymentIntent.create(**intent_data)
        
        return {
            'success': True,
            'client_secret': payment_intent.client_secret,
            'payment_intent_id': payment_intent.id,
            'amount': payment_intent.amount,
            'currency': payment_intent.currency,
            'status': payment_intent.status
        }
    except stripe.error.StripeError as e:
        return {
            'success': False,
            'error': str(e),
            'error_type': type(e).__name__
        }


def create_customer(email: str, name: Optional[str] = None, 
                   phone: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a new Stripe customer
    """
    try:
        customer_data = {'email': email}
        if name:
            customer_data['name'] = name
        if phone:
            customer_data['phone'] = phone
        
        customer = stripe.Customer.create(**customer_data)
        
        return {
            'success': True,
            'customer_id': customer.id,
            'email': customer.email,
            'name': customer.name,
            'created': customer.created
        }
    except stripe.error.StripeError as e:
        return {
            'success': False,
            'error': str(e),
            'error_type': type(e).__name__
        }


def process_refund(payment_intent_id: str, amount: Optional[int] = None) -> Dict[str, Any]:
    """
    Process a refund for a payment
    """
    try:
        refund_data = {'payment_intent': payment_intent_id}
        if amount:
            refund_data['amount'] = amount
        
        refund = stripe.Refund.create(**refund_data)
        
        return {
            'success': True,
            'refund_id': refund.id,
            'amount': refund.amount,
            'currency': refund.currency,
            'status': refund.status
        }
    except stripe.error.StripeError as e:
        return {
            'success': False,
            'error': str(e),
            'error_type': type(e).__name__
        }


if __name__ == '__main__':
    # Example usage
    print("Stripe Payment Processing Script")
    print("=" * 40)
    
    # Test customer creation
    print("\n1. Creating test customer...")
    customer_result = create_customer(
        email="test@example.com",
        name="Test Customer"
    )
    print(json.dumps(customer_result, indent=2))
    
    if customer_result['success']:
        # Test payment intent creation
        print("\n2. Creating payment intent...")
        payment_result = create_payment_intent(
            amount=1999,  # $19.99
            currency='usd',
            customer_id=customer_result.get('customer_id'),
            metadata={'product': 'premium_plan', 'user_id': '123'}
        )
        print(json.dumps(payment_result, indent=2))
