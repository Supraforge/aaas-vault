#!/bin/bash
# Install script for database-schema-validator skill

echo "Installing dependencies for database-schema-validator..."

# Check if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Installing..."
    apt-get update && apt-get install -y python3
fi

echo "✅ database-schema-validator dependencies installed."
