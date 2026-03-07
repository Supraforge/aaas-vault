---
name: api-testing-observability
description: >-
  Creates mock APIs for development and testing, and generates comprehensive API
  documentation with observability features
version: 1.0.0
dependencies:
  - python3
  - fastapi
  - uvicorn
  - pydantic
  - requests
  - httpx
  - openapi-spec-validator
  - swagger-ui
compatibility: 'agent-zero, claude-code, cursor'
---

# API Testing & Observability

## 🎯 Triggers
- "Create a mock API for testing our frontend"
- "Generate comprehensive API documentation with examples"
- "Set up API observability and monitoring"
- "Build an API mocking framework for parallel development"
- "Create OpenAPI specifications with authentication examples"
- "Design interactive API documentation with try-it-now functionality"
- "Generate SDKs in multiple languages from API specs"
- "Implement API testing with realistic mock responses"

## ⚡ Quick Start (Self-Check)
Before running complex API testing or documentation tasks, verify readiness:
- [ ] Run `bash ~/.gemini/skills/api-testing-observability/test.sh` to check dependencies
- [ ] Ensure Python 3.8+ is available
- [ ] Install required packages with `bash ~/.gemini/skills/api-testing-observability/install.sh`

## 📋 Workflow

### 1. **Ingest**: Analyze the API requirements
   - Determine if the task is about API mocking, documentation, or both
   - Identify target API specifications (OpenAPI, GraphQL, REST)
   - Understand authentication requirements and response formats

### 2. **Execute**: Implement the required functionality
   - For API mocking: Create realistic mock servers with dynamic responses
   - For API documentation: Generate comprehensive specs with examples
   - For observability: Add monitoring, logging, and testing frameworks

### 3. **Verify**: Validate the implementation
   - Test mock APIs with sample requests
   - Validate OpenAPI specifications
   - Ensure documentation examples are executable
   - Verify observability metrics are captured

## 🤖 System Instructions

### API Mocking Framework
- Create flexible mock servers that simulate real API behavior
- Support dynamic responses based on request parameters
- Implement state management for realistic testing scenarios
- Include error simulation for robustness testing
- Support multiple authentication methods (JWT, OAuth, API keys)
- Provide configuration for response delays and rate limiting

### API Documentation Generation
- Generate OpenAPI 3.1 specifications from code or descriptions
- Create interactive documentation with Swagger UI or Redoc
- Include comprehensive examples for all endpoints
- Generate SDKs in multiple languages (Python, JavaScript, Go, etc.)
- Implement documentation testing and validation
- Create migration guides for API version updates

### Observability & Testing
- Implement request/response logging
- Add performance metrics collection
- Create automated test suites for API endpoints
- Generate test data and scenarios
- Implement contract testing between services
- Set up monitoring dashboards

## 🛠️ Script Reference

### Mock Server Creation
```python
# Example: Basic mock server setup
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Mock API Server")

@app.get("/api/v1/users")
async def get_users():
    return [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### OpenAPI Specification Generation
```python
# Example: Generate OpenAPI spec
from fastapi.openapi.utils import get_openapi

app = FastAPI()

openapi_schema = get_openapi(
    title="My API",
    version="1.0.0",
    description="API documentation",
    routes=app.routes,
)

# Save to file
import json
with open("openapi.json", "w") as f:
    json.dump(openapi_schema, f, indent=2)
```

## 📊 Quality Standards
- All mock APIs must include comprehensive test coverage
- Documentation must be validated against OpenAPI specifications
- Generated SDKs must include usage examples
- Observability features must include metrics, logs, and traces
- All code examples must be executable and tested

## 🔧 Integration Points
- CI/CD pipelines for automated API testing
- Documentation hosting platforms (ReadMe, GitBook)
- Monitoring tools (Prometheus, Grafana, Datadog)
- API gateways (Kong, Apigee, AWS API Gateway)
- Testing frameworks (pytest, Postman, Newman)
