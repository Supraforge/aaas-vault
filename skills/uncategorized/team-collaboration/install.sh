#!/bin/bash
# Team Collaboration Skill - Installation

echo "📦 Installing team-collaboration skill dependencies..."

# Update package list
apt-get update >/dev/null 2>&1 || true

# Install jq for JSON processing
if ! command -v jq >/dev/null 2>&1; then
    echo "Installing jq..."
    apt-get install -y jq 2>/dev/null || \
        brew install jq 2>/dev/null || \
        echo "⚠️  Could not install jq. Manual installation may be needed."
fi

# Install curl for API calls
if ! command -v curl >/dev/null 2>&1; then
    echo "Installing curl..."
    apt-get install -y curl 2>/dev/null || \
        brew install curl 2>/dev/null || \
        echo "⚠️  Could not install curl. Manual installation may be needed."
fi

# Install Git if not present
if ! command -v git >/dev/null 2>&1; then
    echo "Installing Git..."
    apt-get install -y git 2>/dev/null || \
        brew install git 2>/dev/null || \
        echo "⚠️  Could not install Git. Manual installation may be needed."
fi

# Create scripts directory if needed
mkdir -p scripts 2>/dev/null || true
mkdir -p templates 2>/dev/null || true

echo ""
echo "✅ Team collaboration skill installation complete!"
echo ""
echo "Next steps:"
echo "1. Configure Git user: git config --global user.name 'Your Name'"
echo "2. Configure Git email: git config --global user.email 'your@email.com'"
echo "3. Run test: bash test.sh"
echo ""
echo "For advanced setup:"
echo "• Install Obsidian for note integration"
echo "• Configure Jira API access for ticket tracking"
echo "• Set up calendar integration for meeting context"
