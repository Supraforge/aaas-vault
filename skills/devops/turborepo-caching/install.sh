#!/bin/bash
# Installation script for turborepo-caching

echo "Installing dependencies for turborepo-caching..."

# Update package list
echo "Updating package list..."
apt-get update

# Install Node.js and npm
echo "Installing Node.js and npm..."
apt-get install -y nodejs npm

# Install Git for remote caching
echo "Installing Git..."
apt-get install -y git

# Install Turborepo globally
echo "Installing Turborepo globally..."
npm install -g turbo

echo "✅ Dependencies installed successfully!"
echo "You can now use the turborepo-caching skill."
echo "\nTo get started:"
echo "1. Run: npx create-turbo@latest"
echo "2. Configure turbo.json for your project"
echo "3. Set up remote caching with: npx turbo login"
