#!/usr/bin/env python3
"""
Webhook management for Zapier integration
"""
import os
import json
import hashlib
import hmac
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from dotenv import load_dotenv

load_dotenv()

class WebhookHandler(BaseHTTPRequestHandler):
    """HTTP handler for Zapier webhooks"""
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # Verify webhook signature if secret is set
        webhook_secret = os.getenv('WEBHOOK_SECRET')
        if webhook_secret:
            signature = self.headers.get('X-Zapier-Signature')
            if signature:
                expected = hmac.new(
                    webhook_secret.encode(),
                    post_data,
                    hashlib.sha256
                ).hexdigest()
                
                if not hmac.compare_digest(signature, expected):
                    self.send_response(401)
                    self.end_headers()
                    return
        
        # Process webhook data
        try:
            data = json.loads(post_data.decode('utf-8'))
            print(f"📨 Received webhook: {json.dumps(data, indent=2)}")
            
            # Here you would trigger your zap or process the data
            # For example: zapier.trigger_zap(zap_id, data)
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'status': 'received',
                'message': 'Webhook processed successfully'
            }).encode())
            
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
    
    def log_message(self, format, *args):
        # Suppress default logging
        pass

def start_webhook_server(port=8080):
    """Start webhook server"""
    server = HTTPServer(('0.0.0.0', port), WebhookHandler)
    print(f"🌐 Webhook server listening on port {port}")
    print(f"   Configure Zapier webhook to: http://your-server:{port}/")
    server.serve_forever()

if __name__ == '__main__':
    port = int(os.getenv('WEBHOOK_PORT', 8080))
    
    print(f"🚀 Starting Zapier webhook server on port {port}...")
    print("Press Ctrl+C to stop")
    
    try:
        start_webhook_server(port)
    except KeyboardInterrupt:
        print("\n👋 Webhook server stopped")
