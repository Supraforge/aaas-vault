#!/bin/bash
# Installs necessary dependencies for 3D web development

echo "Installing dependencies for 3D Web Experience skill..."

echo "
1. Checking system dependencies..."
# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Installing Node.js..."
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
    apt-get install -y nodejs
fi

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Installing Python 3..."
    apt-get install -y python3 python3-pip
fi

echo "
2. Installing global npm packages for 3D development..."
npm install -g @splinetool/runtime
npm install -g @gltf-transform/cli

echo "
3. Creating requirements.txt for Python tools..."
cat > requirements.txt << EOF
# Python dependencies for 3D model optimization and analysis
pillow
numpy
EOF

pip3 install -r requirements.txt

echo "
✅ Installation complete!"
echo "Available tools:"
echo "- Spline Runtime: For quick 3D prototypes"
echo "- gltf-transform: For 3D model optimization"
echo "- Python tools: For image/texture processing"
