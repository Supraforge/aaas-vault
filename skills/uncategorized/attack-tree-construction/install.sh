#!/bin/bash
# Install script for attack-tree-construction skill

echo "Installing dependencies for attack-tree-construction..."

# Check if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is required but not installed. Installing..."
    apt-get update && apt-get install -y python3 python3-pip
fi

# Optional: Install graphviz for visualization if needed
# echo "Installing graphviz for visualization support..."
# apt-get install -y graphviz

echo "✅ Dependencies installed."
echo "This skill provides templates and frameworks for building attack trees to visualize threat paths."
echo "The skill includes Python data models, Mermaid diagram generators, and attack path analysis tools."
