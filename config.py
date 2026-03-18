import os
import dotenv

# Configuration for EUR currency
CURRENCY = 'EUR'

# Stripe Configuration
STRIPE_API_KEY = 'your_stripe_api_key'
STRIPE_PUBLIC_KEY = 'your_stripe_public_key'

# PayPal Configuration
PAYPAL_CLIENT_ID = 'your_paypal_client_id'
PAYPAL_SECRET = 'your_paypal_secret'

# Load environment variables
dotenv.load_dotenv()