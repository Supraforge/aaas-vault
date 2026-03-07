---
name: backend-scaffolding
description: >-
  Scaffolds production-ready backend projects with FastAPI, Django, GraphQL, and
  modern architecture patterns. Use when starting new backend applications or
  refactoring existing ones.
version: 1.0.0
dependencies:
  - python3
  - uv
  - git
  - docker
  - docker-compose
compatibility: 'agent-zero, claude-code, cursor'
---

# Backend Scaffolding Skill

## 🎯 Triggers
- "Create a new FastAPI project with async patterns"
- "Set up a Django 5.x project with DRF and Celery"
- "Design a scalable backend architecture"
- "Implement GraphQL API with proper subscriptions"
- "Scaffold a production-ready backend with testing and deployment"
- "Migrate from REST to GraphQL"
- "Implement microservices patterns"

## ⚡ Quick Start (Self-Check)
Before running complex logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/backend-scaffolding/test.sh` to check dependencies.
- [ ] Ensure Python 3.8+ is installed: `python3 --version`
- [ ] Check for Docker: `docker --version`
- [ ] Verify Git: `git --version`

## 📋 Workflow

### 1. Framework Selection
**Analyze requirements:** Determine which backend framework best fits the project:
- **FastAPI**: For high-performance async APIs, microservices, and modern Python
- **Django**: For full-featured web applications with admin, ORM, and batteries included
- **GraphQL**: For complex data relationships and flexible querying
- **Hybrid**: Combine multiple approaches as needed

### 2. Project Structure Generation
**Create standardized layouts:**
- FastAPI: Async patterns, dependency injection, OpenAPI docs
- Django: Modular apps, settings management, DRF integration
- GraphQL: Schema-first design, resolver patterns, subscriptions
- Common: Testing setup, Docker configuration, CI/CD templates

### 3. Architecture Implementation
**Apply patterns:**
- Repository and service layer patterns
- Dependency injection and inversion of control
- Event-driven architecture with message queues
- CQRS and Event Sourcing when appropriate
- Microservices communication patterns

### 4. Security & Authentication
**Implement security:**
- OAuth2/JWT authentication
- Role-based access control (RBAC)
- Input validation and sanitization
- Rate limiting and DDoS protection
- Security headers and CORS configuration

### 5. Database & Data Layer
**Configure data access:**
- SQLAlchemy 2.0+ with async support
- Django ORM with optimization patterns
- Database migrations (Alembic, Django Migrations)
- Connection pooling and session management
- Redis caching and session storage

### 6. Testing & Quality
**Set up testing:**
- Unit, integration, and end-to-end tests
- Mocking strategies for external services
- Performance and load testing
- Security scanning and dependency checking
- Code coverage and quality gates

### 7. Deployment & DevOps
**Prepare for production:**
- Docker and Docker Compose configurations
- Kubernetes manifests for scaling
- CI/CD pipeline templates
- Monitoring and observability setup
- Logging and error tracking

## 🤖 System Instructions

### FastAPI Specialization
- Use async/await patterns for I/O-bound operations
- Implement dependency injection with FastAPI's Depends()
- Generate automatic OpenAPI/Swagger documentation
- Implement WebSocket endpoints for real-time features
- Use Pydantic V2 for data validation and serialization
- Configure CORS middleware properly
- Implement background tasks with Celery or BackgroundTasks

### Django Specialization
- Follow Django's "batteries included" philosophy
- Use class-based views (CBVs) for reusable patterns
- Optimize ORM queries with select_related and prefetch_related
- Implement Django REST Framework (DRF) for APIs
- Use Django Channels for WebSocket support
- Configure Django Admin for data management
- Implement custom middleware when needed

### GraphQL Specialization
- Design schema-first with proper types and interfaces
- Implement efficient resolver patterns
- Set up subscriptions for real-time updates
- Use DataLoader for N+1 query prevention
- Implement authentication and authorization
- Add query complexity analysis and rate limiting
- Provide GraphiQL/Playground for development

### Architecture Patterns
- Apply Clean Architecture or Hexagonal Architecture
- Separate business logic from framework code
- Implement repository and unit of work patterns
- Use event-driven architecture for decoupling
- Implement circuit breaker for external service calls
- Apply CQRS for complex write/read separation

## 🛠️ Script Reference

### Project Templates
- Use `templates/fastapi-project/` for FastAPI scaffolding
- Use `templates/django-project/` for Django scaffolding
- Use `templates/graphql-project/` for GraphQL scaffolding
- Use `templates/microservices/` for distributed systems

### Utility Scripts
- `scripts/setup-fastapi.sh`: Creates FastAPI project structure
- `scripts/setup-django.sh`: Creates Django project structure
- `scripts/setup-graphql.sh`: Creates GraphQL project structure
- `scripts/add-feature.sh`: Adds new feature modules
- `scripts/generate-tests.sh`: Creates test boilerplate

### Health Checks
- `scripts/check-dependencies.sh`: Verifies system requirements
- `scripts/validate-architecture.sh`: Validates project structure
- `scripts/run-smoke-tests.sh`: Runs basic functionality tests

## 📁 Generated Files Structure

### FastAPI Project
```
project/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   └── router.py
│   │   └── dependencies.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── database.py
│   ├── models/
│   ├── schemas/
│   └── services/
├── tests/
├── docker/
├── alembic/
├── requirements.txt
└── docker-compose.yml
```

### Django Project
```
project/
├── config/
│   ├── settings/
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── users/
│   ├── api/
│   └── common/
├── static/
├── templates/
├── tests/
├── manage.py
└── requirements.txt
```

### GraphQL Project
```
project/
├── schema/
│   ├── types/
│   ├── queries/
│   ├── mutations/
│   └── subscriptions/
├── resolvers/
├── dataloaders/
├── middleware/
├── tests/
└── server.py
```

## 🔧 Dependencies Management

### Python Dependencies
- FastAPI: fastapi, uvicorn, pydantic, sqlalchemy, alembic
- Django: django, djangorestframework, django-cors-headers
- GraphQL: strawberry, graphene, ariadne
- Common: python-jose, redis, celery, pytest

### Development Tools
- UV for Python package management
- Pre-commit for code quality
- Black, isort, flake8 for formatting
- MyPy for type checking
- Bandit for security scanning

## 🚀 Getting Started

1. **Choose framework:** Determine which backend approach fits your needs
2. **Run health check:** `bash ~/.gemini/skills/backend-scaffolding/test.sh`
3. **Generate project:** Use the appropriate setup script
4. **Customize:** Modify generated files for your specific requirements
5. **Verify:** Run tests and validate the project structure

## 📚 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Django Documentation](https://docs.djangoproject.com/)
- [GraphQL Official Docs](https://graphql.org/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Microservices Patterns](https://microservices.io/)
