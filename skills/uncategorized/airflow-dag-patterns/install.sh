#!/bin/bash
# Installation script for airflow-dag-patterns

echo "Installing dependencies for airflow-dag-patterns..."

# Check if pip is available
if command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
elif command -v pip &> /dev/null; then
    PIP_CMD="pip"
else
    echo "❌ pip not found. Installing pip..."
    apt-get update && apt-get install -y python3-pip
    PIP_CMD="pip3"
fi

# Install Apache Airflow
echo "Installing Apache Airflow..."
$PIP_CMD install apache-airflow

if [ $? -eq 0 ]; then
    echo "✅ Apache Airflow installed successfully."
else
    echo "❌ Failed to install Apache Airflow."
    exit 1
fi

echo "✅ All dependencies installed."
