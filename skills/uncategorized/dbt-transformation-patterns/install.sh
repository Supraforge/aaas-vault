#!/bin/bash
# Installation script for dbt-transformation-patterns

echo "Installing dependencies for dbt-transformation-patterns..."

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

# Install dbt-core
echo "Installing dbt-core..."
$PIP_CMD install dbt-core

# Optionally install adapters based on database
# $PIP_CMD install dbt-postgres  # For PostgreSQL
# $PIP_CMD install dbt-snowflake  # For Snowflake
# $PIP_CMD install dbt-bigquery  # For BigQuery

if [ $? -eq 0 ]; then
    echo "✅ dbt-core installed successfully."
    echo "Note: You may need to install a specific adapter for your database."
    echo "Common adapters: dbt-postgres, dbt-snowflake, dbt-bigquery"
else
    echo "❌ Failed to install dbt-core."
    exit 1
fi

echo "✅ All dependencies installed."
