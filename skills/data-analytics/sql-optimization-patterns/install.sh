#!/bin/bash
# Installation script for sql-optimization-patterns

echo "Installing dependencies for sql-optimization-patterns..."

# Update package list
echo "Updating package list..."
apt-get update

# Install database clients
echo "Installing database clients..."
apt-get install -y sqlite3 postgresql-client mysql-client

echo "✅ Dependencies installed successfully!"
echo "You can now use the sql-optimization-patterns skill."
