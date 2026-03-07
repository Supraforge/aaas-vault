#!/bin/bash
# Install dependencies for Microsoft Ads MCP skill

echo "📦 Installing Microsoft Ads MCP dependencies..."

# Create virtual environment for Python
if [ ! -d "venv" ]; then
    echo "🐍 Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install Python packages
if [ -f "requirements.txt" ]; then
    echo "📦 Installing Python dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    # Create requirements.txt with essential packages
    cat > requirements.txt << 'REQEOF'
# Microsoft Advertising SDK
bingads==13.0.15

# Data processing
pandas>=1.5.0
numpy>=1.24.0
openpyxl>=3.1.0

# API and web
requests>=2.28.0
httpx>=0.24.0
aiohttp>=3.8.0

# Utilities
dotenv>=1.0.0
python-dateutil>=2.8.0
pytz>=2023.0

# Reporting
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.14.0

# CLI
click>=8.1.0
rich>=13.0.0
tabulate>=0.9.0

# Testing
pytest>=7.0.0
pytest-asyncio>=0.21.0
REQEOF
    
    echo "📦 Installing Python dependencies from generated requirements.txt..."
    pip install --upgrade pip
    pip install -r requirements.txt
fi

# Install Node.js dependencies if package.json exists
if [ -f "scripts/package.json" ]; then
    echo "📦 Installing Node.js dependencies..."
    cd scripts
    npm install --silent
    cd ..
fi

# Create necessary directories
mkdir -p logs reports data exports

# Install Bing Ads SDK if not available via pip
if ! python3 -c "import bingads" 2>/dev/null; then
    echo "🔧 Installing Bing Ads SDK..."
    pip install bingads
fi

echo "\n✅ Installation complete!"
echo "\n📋 Next steps:"
echo "1. Copy .env.template to .env"
echo "2. Add your Microsoft Advertising API credentials to .env"
echo "3. Run ./test.sh to verify setup"
echo "4. Activate virtual environment: source venv/bin/activate"
