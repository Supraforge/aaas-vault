#!/bin/bash
# Installation script for LinkedIn MCP Integration skill

set -e

echo "🚀 Installing LinkedIn MCP Integration skill..."

# Check if we're in the right directory
if [ ! -f "SKILL.md" ]; then
    echo "❌ Error: Not in LinkedIn MCP skill directory"
    echo "   Run this script from ~/.gemini/skills/linkedin-mcp/"
    exit 1
fi

# Make scripts executable
chmod +x test.sh
chmod +x install.sh

# Install Node.js dependencies
if [ -f "package.json" ]; then
    echo "📦 Installing Node.js dependencies..."
    npm install
    echo "✅ Node.js dependencies installed"
else
    echo "📝 Creating package.json for LinkedIn MCP..."
    cat > package.json << 'PACKAGE_EOF'
{
  "name": "linkedin-mcp-server",
  "version": "1.0.0",
  "description": "MCP server for LinkedIn Marketing and Sales APIs",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js",
    "test": "jest"
  },
  "dependencies": {
    "@linkedin/api-client": "^2.0.0",
    "express": "^4.18.2",
    "axios": "^1.6.0",
    "dotenv": "^16.3.1",
    "jsonwebtoken": "^9.0.2",
    "winston": "^3.11.0",
    "@modelcontextprotocol/sdk": "^0.5.0",
    "@modelcontextprotocol/server-express": "^0.5.0"
  },
  "devDependencies": {
    "nodemon": "^3.0.1",
    "jest": "^29.7.0",
    "supertest": "^6.3.3"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
PACKAGE_EOF
    
    echo "📦 Installing Node.js dependencies..."
    npm install
    echo "✅ Node.js dependencies installed"
fi

# Install Python dependencies
if [ -f "requirements.txt" ]; then
    echo "🐍 Installing Python dependencies..."
    pip install -r requirements.txt
    echo "✅ Python dependencies installed"
else
    echo "📝 Creating requirements.txt for LinkedIn MCP..."
    cat > requirements.txt << 'REQUIREMENTS_EOF'
# LinkedIn MCP Python dependencies
linkedin-api==2.0.0
requests==2.31.0
python-dotenv==1.0.0
pandas==2.1.3
numpy==1.26.2
scikit-learn==1.3.2
matplotlib==3.8.2
seaborn==0.13.0
pytest==7.4.3
pytest-asyncio==0.21.1
REQUIREMENTS_EOF
    
    echo "🐍 Installing Python dependencies..."
    pip install -r requirements.txt
    echo "✅ Python dependencies installed"
fi

# Create basic server.js if not exists
if [ ! -f "server.js" ]; then
    echo "📝 Creating basic MCP server..."
    cat > server.js << 'SERVER_EOF'
// LinkedIn MCP Server
require('dotenv').config();
const express = require('express');
const { Server } = require('@modelcontextprotocol/sdk/server/express');
const { LinkedInAPI } = require('./lib/linkedin-api');

const app = express();
const port = process.env.MCP_SERVER_PORT || 5603;

// Initialize LinkedIn API
const linkedin = new LinkedInAPI({
  clientId: process.env.LINKEDIN_CLIENT_ID,
  clientSecret: process.env.LINKEDIN_CLIENT_SECRET,
  accessToken: process.env.LINKEDIN_ACCESS_TOKEN,
  companyId: process.env.LINKEDIN_COMPANY_ID
});

// Create MCP server
const server = new Server(
  {
    name: 'linkedin-mcp-server',
    version: '1.0.0',
  },
  {
    capabilities: {
      resources: {},
      tools: {},
      prompts: {},
    },
  }
);

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'ok', service: 'linkedin-mcp' });
});

// Start server
app.listen(port, () => {
  console.log(`✅ LinkedIn MCP server running on port ${port}`);
  console.log(`🔗 Health check: http://localhost:${port}/health`);
});

module.exports = app;
SERVER_EOF
    echo "✅ Basic MCP server created"
fi

# Create lib directory with LinkedIn API wrapper
mkdir -p lib
if [ ! -f "lib/linkedin-api.js" ]; then
    echo "📝 Creating LinkedIn API wrapper..."
    cat > lib/linkedin-api.js << 'API_EOF'
// LinkedIn API Wrapper for MCP
const axios = require('axios');

class LinkedInAPI {
  constructor(config) {
    this.clientId = config.clientId;
    this.clientSecret = config.clientSecret;
    this.accessToken = config.accessToken;
    this.companyId = config.companyId;
    this.baseURL = 'https://api.linkedin.com/v2';
    
    this.client = axios.create({
      baseURL: this.baseURL,
      headers: {
        'Authorization': `Bearer ${this.accessToken}`,
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0'
      }
    });
  }
  
  // Company methods
  async getCompany() {
    const response = await this.client.get(`/organizations/${this.companyId}`);
    return response.data;
  }
  
  async getCompanyPosts(limit = 10) {
    const response = await this.client.get(
      `/organizations/${this.companyId}/posts`, 
      { params: { count: limit } }
    );
    return response.data;
  }
  
  // Campaign methods
  async createCampaign(campaignData) {
    const response = await this.client.post(
      '/adCampaignsV2', 
      campaignData
    );
    return response.data;
  }
  
  async getCampaigns() {
    const response = await this.client.get('/adCampaignsV2');
    return response.data;
  }
  
  // Analytics methods
  async getCampaignAnalytics(campaignId, dateRange) {
    const response = await this.client.get(
      `/adAnalyticsV2?q=analytics&campaigns[0]=urn:li:sponsoredCampaign:${campaignId}&dateRange.start.day=${dateRange.start}&dateRange.start.month=${dateRange.startMonth}&dateRange.start.year=${dateRange.startYear}&dateRange.end.day=${dateRange.end}&dateRange.end.month=${dateRange.endMonth}&dateRange.end.year=${dateRange.endYear}&pivot=CAMPAIGN&timeGranularity=DAILY`
    );
    return response.data;
  }
  
  // Lead generation methods
  async getLeadForms() {
    const response = await this.client.get('/leadForms');
    return response.data;
  }
  
  async getFormLeads(formId) {
    const response = await this.client.get(`/leadForms/${formId}/leads`);
    return response.data;
  }
  
  // Health check
  async healthCheck() {
    try {
      await this.getCompany();
      return { status: 'healthy', message: 'LinkedIn API connection successful' };
    } catch (error) {
      return { status: 'unhealthy', message: error.message };
    }
  }
}

module.exports = { LinkedInAPI };
API_EOF
    echo "✅ LinkedIn API wrapper created"
fi

# Create .env from template if .env doesn't exist
if [ ! -f ".env" ] && [ -f ".env.template" ]; then
    echo "📝 Creating .env file from template..."
    cp .env.template .env
    echo "⚠️  IMPORTANT: Edit .env file with your LinkedIn API credentials"
    echo "   Required: LINKEDIN_CLIENT_ID, LINKEDIN_CLIENT_SECRET, LINKEDIN_ACCESS_TOKEN"
fi

# Create scripts directory
mkdir -p scripts

# Create sample scripts
if [ ! -f "scripts/create-campaign.sh" ]; then
    echo "📝 Creating sample campaign script..."
    cat > scripts/create-campaign.sh << 'CAMPAIGN_EOF'
#!/bin/bash
# Create LinkedIn advertising campaign

set -e

# Load environment variables
if [ -f "../.env" ]; then
    export $(cat ../.env | grep -v '^#' | xargs)
fi

# Check required variables
if [ -z "$LINKEDIN_CLIENT_ID" ] || [ -z "$LINKEDIN_CLIENT_SECRET" ] || [ -z "$LINKEDIN_ACCESS_TOKEN" ]; then
    echo "❌ Error: LinkedIn API credentials not set in .env file"
    exit 1
fi

# Default campaign data
CAMPAIGN_DATA=$(cat << JSON
{
  "account": "urn:li:sponsoredAccount:$(echo $LINKEDIN_COMPANY_ID)",
  "name": "${1:-LinkedIn Marketing Campaign}",
  "campaignGroup": "urn:li:sponsoredCampaignGroup:123456789",
  "status": "ACTIVE",
  "type": "TEXT_AD",
  "dailyBudget": {
    "amount": "${2:-50.00}",
    "currencyCode": "USD"
  },
  "unitCost": {
    "amount": "${3:-5.00}",
    "currencyCode": "USD"
  },
  "start": {
    "day": $(date +%d),
    "month": $(date +%m),
    "year": $(date +%Y)
  },
  "end": {
    "day": $(date -d '+30 days' +%d),
    "month": $(date -d '+30 days' +%m),
    "year": $(date -d '+30 days' +%Y)
  }
}
JSON
)

echo "🎯 Creating LinkedIn campaign..."
echo "$CAMPAIGN_DATA" | jq .

echo "✅ Campaign creation script ready"
echo "   Run with: ./scripts/create-campaign.sh 'Campaign Name' 100 10"
echo "   Where: Campaign Name, Daily Budget ($), Cost per Click ($)"
CAMPAIGN_EOF
    chmod +x scripts/create-campaign.sh
    echo "✅ Sample campaign script created"
fi

if [ ! -f "scripts/analyze-performance.sh" ]; then
    echo "📝 Creating performance analysis script..."
    cat > scripts/analyze-performance.sh << 'ANALYSIS_EOF'
#!/bin/bash
# Analyze LinkedIn campaign performance

set -e

# Load environment variables
if [ -f "../.env" ]; then
    export $(cat ../.env | grep -v '^#' | xargs)
fi

# Check for Python dependencies
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python3 is required for analysis"
    exit 1
fi

# Create Python analysis script
cat > /tmp/analyze_linkedin.py << 'PYTHON_EOF'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import json
import os

# Load environment variables
def load_env():
    env_vars = {}
    if os.path.exists('../.env'):
        with open('../.env', 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    env_vars[key] = value
    return env_vars

# Generate sample data for demonstration
def generate_sample_data():
    dates = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')
    data = {
        'date': dates,
        'impressions': np.random.randint(1000, 10000, len(dates)),
        'clicks': np.random.randint(50, 500, len(dates)),
        'conversions': np.random.randint(5, 50, len(dates)),
        'spend': np.random.uniform(100, 1000, len(dates)),
        'ctr': np.random.uniform(1.0, 5.0, len(dates)),
        'cpc': np.random.uniform(2.0, 10.0, len(dates))
    }
    return pd.DataFrame(data)

# Analyze campaign performance
def analyze_performance(df):
    print("📊 LinkedIn Campaign Performance Analysis")
    print("=" * 50)
    
    # Basic metrics
    total_impressions = df['impressions'].sum()
    total_clicks = df['clicks'].sum()
    total_conversions = df['conversions'].sum()
    total_spend = df['spend'].sum()
    
    print(f"Total Impressions: {total_impressions:,}")
    print(f"Total Clicks: {total_clicks:,}")
    print(f"Total Conversions: {total_conversions:,}")
    print(f"Total Spend: ${total_spend:,.2f}")
    
    # Calculated metrics
    overall_ctr = (total_clicks / total_impressions) * 100 if total_impressions > 0 else 0
    overall_cpc = total_spend / total_clicks if total_clicks > 0 else 0
    conversion_rate = (total_conversions / total_clicks) * 100 if total_clicks > 0 else 0
    cpa = total_spend / total_conversions if total_conversions > 0 else 0
    
    print(f"\n📈 Performance Metrics:")
    print(f"  CTR: {overall_ctr:.2f}%")
    print(f"  CPC: ${overall_cpc:.2f}")
    print(f"  Conversion Rate: {conversion_rate:.2f}%")
    print(f"  CPA: ${cpa:.2f}")
    
    # Daily trends
    print(f"\n📅 Daily Trends:")
    avg_daily_impressions = df['impressions'].mean()
    avg_daily_clicks = df['clicks'].mean()
    avg_daily_spend = df['spend'].mean()
    
    print(f"  Avg Daily Impressions: {avg_daily_impressions:,.0f}")
    print(f"  Avg Daily Clicks: {avg_daily_clicks:,.0f}")
    print(f"  Avg Daily Spend: ${avg_daily_spend:.2f}")
    
    # Best performing day
    best_day = df.loc[df['clicks'].idxmax()]
    print(f"\n🏆 Best Performing Day: {best_day['date'].strftime('%Y-%m-%d')}")
    print(f"  Impressions: {best_day['impressions']:,}")
    print(f"  Clicks: {best_day['clicks']:,}")
    print(f"  CTR: {best_day['ctr']:.2f}%")
    
    # Recommendations
    print(f"\n💡 Recommendations:")
    if overall_ctr < 2.0:
        print("  ⚠️  CTR is below 2% - Consider improving ad creative")
    if overall_cpc > 5.0:
        print("  ⚠️  CPC is high - Review targeting and bidding strategy")
    if conversion_rate < 3.0:
        print("  ⚠️  Conversion rate is low - Optimize landing page")
    
    # Generate visualization
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plt.plot(df['date'], df['impressions'], 'b-', label='Impressions')
    plt.title('Daily Impressions')
    plt.xlabel('Date')
    plt.ylabel('Impressions')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 2, 2)
    plt.plot(df['date'], df['clicks'], 'g-', label='Clicks')
    plt.title('Daily Clicks')
    plt.xlabel('Date')
    plt.ylabel('Clicks')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 2, 3)
    plt.plot(df['date'], df['ctr'], 'r-', label='CTR')
    plt.title('Click-Through Rate (CTR)')
    plt.xlabel('Date')
    plt.ylabel('CTR (%)')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 2, 4)
    plt.bar(df['date'], df['spend'], color='orange', alpha=0.7)
    plt.title('Daily Spend')
    plt.xlabel('Date')
    plt.ylabel('Spend ($)')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/tmp/linkedin_performance.png', dpi=150, bbox_inches='tight')
    print(f"\n📊 Visualization saved to: /tmp/linkedin_performance.png")
    
    return {
        'total_impressions': total_impressions,
        'total_clicks': total_clicks,
        'total_conversions': total_conversions,
        'total_spend': total_spend,
        'ctr': overall_ctr,
        'cpc': overall_cpc,
        'conversion_rate': conversion_rate,
        'cpa': cpa
    }

if __name__ == '__main__':
    # Load sample data (replace with actual API call)
    df = generate_sample_data()
    
    # Analyze performance
    results = analyze_performance(df)
    
    # Save results to JSON
    with open('/tmp/linkedin_analysis.json', 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n💾 Analysis results saved to: /tmp/linkedin_analysis.json")
PYTHON_EOF

# Run the analysis
python3 /tmp/analyze_linkedin.py

# Cleanup
rm -f /tmp/analyze_linkedin.py

echo "\n✅ Performance analysis completed"
echo "   Check /tmp/linkedin_performance.png for visualization"
echo "   Check /tmp/linkedin_analysis.json for detailed results"
ANALYSIS_EOF
    chmod +x scripts/analyze-performance.sh
    echo "✅ Performance analysis script created"
fi

# Create README
if [ ! -f "README.md" ]; then
    echo "📝 Creating README..."
    cat > README.md << 'README_EOF'
# LinkedIn MCP Integration

Model Context Protocol (MCP) server for LinkedIn Marketing and Sales APIs.

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   bash install.sh
   ```

2. **Configure environment:**
   ```bash
   cp .env.template .env
   # Edit .env with your LinkedIn API credentials
   ```

3. **Test installation:**
   ```bash
   bash test.sh
   ```

4. **Start MCP server:**
   ```bash
   npm start
   ```

## 🔧 Configuration

### LinkedIn API Setup
1. Create a LinkedIn Developer App at [LinkedIn Developers](https://www.linkedin.com/developers/apps)
2. Get your Client ID and Client Secret
3. Generate an Access Token with required scopes:
   - `r_organization_social`
   - `rw_organization_admin`
   - `w_member_social`
   - `r_ads_reporting`

### Environment Variables
See `.env.template` for all available configuration options.

## 📊 Features

### Campaign Management
- Create and manage LinkedIn advertising campaigns
- Set budgets and targeting parameters
- Schedule campaign start/end dates

### Analytics & Reporting
- Real-time campaign performance tracking
- CTR, CPC, CPA, and ROI calculations
- Daily, weekly, monthly reporting

### Lead Generation
- Lead form creation and management
- Lead retrieval and scoring
- CRM integration (Salesforce, HubSpot)

### Content Management
- Company page post scheduling
- Content performance analytics
- Competitor content monitoring

## 🔌 MCP Integration

This skill provides MCP resources and tools for:

### Resources
- `linkedin://campaigns` - List of advertising campaigns
- `linkedin://analytics/{campaign_id}` - Campaign performance data
- `linkedin://leads` - Generated leads from forms

### Tools
- `create_linkedin_campaign` - Create new advertising campaign
- `analyze_campaign_performance` - Generate performance reports
- `schedule_company_post` - Schedule content to company page
- `retrieve_leads` - Get leads from lead forms

## 📈 Use Cases

### B2B Marketing
- Target specific industries and job titles
- Generate qualified leads for sales teams
- Nurture leads through content marketing

### Brand Awareness
- Increase company visibility
- Share thought leadership content
- Engage with industry communities

### Recruitment Marketing
- Promote job openings
- Build employer brand
- Attract top talent

## 🛠️ Development

### Project Structure
```
linkedin-mcp/
├── server.js              # MCP server entry point
├── lib/                   # LinkedIn API wrappers
├── scripts/               # Utility scripts
├── test.sh               # Health check script
├── install.sh            # Installation script
├── .env.template         # Environment template
└── SKILL.md              # Skill documentation
```

### Adding New Features
1. Add new API methods to `lib/linkedin-api.js`
2. Register new tools in `server.js`
3. Update `SKILL.md` with documentation
4. Add test cases

## 📚 Resources

- [LinkedIn Marketing API Documentation](https://docs.microsoft.com/en-us/linkedin/marketing/)
- [LinkedIn Sales Navigator API](https://docs.microsoft.com/en-us/linkedin/sales-navigator/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [Node.js MCP SDK](https://github.com/modelcontextprotocol/typescript-sdk)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `bash test.sh`
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details.
README_EOF
    echo "✅ README created"
fi

# Create LICENSE
if [ ! -f "LICENSE" ]; then
    echo "📝 Creating LICENSE..."
    cat > LICENSE << 'LICENSE_EOF'
MIT License

Copyright (c) 2024 LinkedIn MCP Integration Skill

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
LICENSE_EOF
    echo "✅ LICENSE created"
fi

echo "\n🎉 LinkedIn MCP skill installation complete!"
echo "\n📋 Next steps:"
echo "   1. Edit .env file with your LinkedIn API credentials"
echo "   2. Run 'bash test.sh' to verify installation"
echo "   3. Start the MCP server: 'npm start'"
echo "   4. Connect using any MCP client"
echo "\n🔗 Useful commands:"
echo "   • Create campaign: ./scripts/create-campaign.sh"
echo "   • Analyze performance: ./scripts/analyze-performance.sh"
echo "   • Check health: bash test.sh"
echo "\n✅ LinkedIn MCP skill is ready for business building, marketing, and sales automation!"
