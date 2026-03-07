"""
Zapier API client for Node.js
"""
const axios = require('axios');

class ZapierAPI {
  constructor(apiKey) {
    this.apiKey = apiKey;
    this.baseUrl = 'https://api.zapier.com/v2';
    this.client = axios.create({
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      }
    });
  }

  async listZaps() {
    const response = await this.client.get(`${this.baseUrl}/zaps`);
    return response.data;
  }

  async getZap(zapId) {
    const response = await this.client.get(`${this.baseUrl}/zaps/${zapId}`);
    return response.data;
  }

  async triggerZap(zapId, data) {
    const response = await this.client.post(
      `${this.baseUrl}/zaps/${zapId}/trigger`,
      data
    );
    return response.data;
  }

  async getExecutions(zapId, limit = 10) {
    const response = await this.client.get(
      `${this.baseUrl}/zaps/${zapId}/executions`,
      { params: { limit } }
    );
    return response.data;
  }

  async createWebhookZap(name, triggerApp, actionApp) {
    const zapData = {
      name,
      trigger: {
        type: 'webhook',
        app: triggerApp
      },
      action: {
        type: 'action',
        app: actionApp
      }
    };
    
    const response = await this.client.post(
      `${this.baseUrl}/zaps`,
      zapData
    );
    return response.data;
  }

  async testConnection() {
    try {
      const response = await this.client.get(
        `${this.baseUrl}/zaps`,
        { params: { limit: 1 } }
      );
      return response.status === 200;
    } catch (error) {
      return false;
    }
  }
}

module.exports = { ZapierAPI };
