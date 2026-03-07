#!/bin/bash
# Autonomous Health Check for Founder Assets

echo "🔍 Validating Founder Assets..."

# Check if the profile JSON exists
if [ -f "$(dirname "$0")/templates/founder_profile.json" ]; then
    echo "✅ Founder Profile (Source of Truth) located."
else
    echo "❌ Error: 'founder_profile.json' is missing. The agent has no memory of you."
    exit 1
fi

echo "🚀 Asset Manager ready. Identity loaded."
