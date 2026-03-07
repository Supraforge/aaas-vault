#!/bin/bash
# Installation script for orchestrating-agents skill

echo "🔧 Installing orchestrating-agents skill dependencies..."

# Function to check and install dependencies
check_dependency() {
    local dep=$1
    local install_cmd=$2
    
    if command -v "$dep" >/dev/null 2>&1; then
        echo "✅ $dep already installed"
        return 0
    else
        echo "⚠️  $dep not found"
        if [ -n "$install_cmd" ]; then
            echo "   Attempting to install with: $install_cmd"
            eval "$install_cmd"
            if command -v "$dep" >/dev/null 2>&1; then
                echo "✅ $dep installed successfully"
                return 0
            else
                echo "❌ Failed to install $dep"
                return 1
            fi
        else
            echo "   Please install $dep manually"
            return 1
        fi
    fi
}

# Check and install dependencies
check_dependency "python3" "apt-get update && apt-get install -y python3"
check_dependency "jq" "apt-get update && apt-get install -y jq"
check_dependency "git" "apt-get update && apt-get install -y git"

# Create scripts directory if it doesn't exist
if [ ! -d "scripts" ]; then
    mkdir -p scripts
    echo "📁 Created scripts directory"
    
    # Create sample orchestration script
    cat > scripts/orchestrate-agents.py << 'PYEOF'
#!/usr/bin/env python3
"""
Sample agent orchestration script
"""
import json
import subprocess
import sys

def check_agent_status():
    """Check if agents are available and responsive"""
    print("Checking agent status...")
    # Add your agent status checking logic here
    return True

def optimize_agent_performance(agent_name):
    """Optimize performance for a specific agent"""
    print(f"Optimizing performance for {agent_name}...")
    # Add optimization logic here
    return {"status": "optimized", "agent": agent_name}

def coordinate_multiple_agents(tasks):
    """Coordinate multiple agents for parallel task execution"""
    print(f"Coordinating {len(tasks)} agents for {len(tasks)} tasks...")
    results = []
    for task in tasks:
        # Add coordination logic here
        results.append({"task": task, "status": "assigned"})
    return results

if __name__ == "__main__":
    print("Agent Orchestration Script")
    print("=========================")
    
    # Example usage
    if check_agent_status():
        print("✅ All agents are ready")
        
        # Optimize a sample agent
        result = optimize_agent_performance("code-review-agent")
        print(f"Optimization result: {result}")
        
        # Coordinate multiple agents
        tasks = ["analyze-code", "run-tests", "generate-docs"]
        coordination_results = coordinate_multiple_agents(tasks)
        print(f"Coordination results: {coordination_results}")
    else:
        print("❌ Some agents are not ready")
        sys.exit(1)
PYEOF
    
    chmod +x scripts/orchestrate-agents.py
    echo "📄 Created sample orchestration script"
fi

echo "\n🎉 Installation complete!"
echo "Run './test.sh' to verify the skill is ready."
echo "\n📋 Available scripts:"
echo "- scripts/orchestrate-agents.py: Sample orchestration script"

exit 0
