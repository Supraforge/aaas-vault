---
name: test-automation
description: >-
  Master AI-powered test automation with modern frameworks, self-healing tests,
  and comprehensive quality engineering. Build scalable testing strategies with
  advanced CI/CD integration.
version: 1.0.0
dependencies:
  - python3
  - nodejs
  - playwright
  - selenium
  - postman
  - k6
  - docker
  - git
compatibility: 'agent-zero, claude-code, cursor'
---

# Test Automation Mastery

## 🎯 Triggers
- "Design a comprehensive test automation strategy for our microservices architecture"
- "Implement AI-powered visual regression testing for our web application"
- "Create a scalable API testing framework with contract validation"
- "Build self-healing UI tests that adapt to application changes"
- "Set up performance testing pipeline with automated threshold validation"
- "Implement cross-browser testing with parallel execution in CI/CD"
- "Create a test data management strategy for multiple environments"
- "Design chaos engineering tests for system resilience validation"
- "Generate failing tests for a new feature following TDD principles"
- "Set up TDD cycle tracking with red-green-refactor metrics"

## ⚡ Quick Start (Self-Check)
Before running complex test automation, verify readiness:
- [ ] Run `bash ~/.gemini/skills/test-automation/test.sh` to check dependencies.
- [ ] Ensure Docker is running for containerized testing environments.
- [ ] Verify network access to testing platforms and APIs.

## 📋 Workflow

### 1. **Analyze Testing Requirements**
- Identify automation opportunities based on application architecture
- Determine appropriate testing frameworks and tools
- Assess existing test coverage and identify gaps
- Define quality gates and acceptance criteria

### 2. **Design Comprehensive Test Strategy**
- Select modern testing frameworks (Playwright, Selenium, Appium, etc.)
- Design AI-powered testing with self-healing capabilities
- Plan CI/CD integration with parallel execution
- Create test data management and environment strategy
- Define performance and security testing requirements

### 3. **Implement Scalable Automation**
- Set up test automation framework with maintainable architecture
- Implement cross-browser and cross-platform testing
- Create API testing with contract validation
- Build performance testing with K6 or JMeter
- Integrate visual regression testing with AI tools
- Implement database testing and validation

### 4. **Integrate with CI/CD Pipelines**
- Configure Jenkins, GitLab CI, or GitHub Actions for test execution
- Implement parallel test execution and optimization
- Set up dynamic test selection based on code changes
- Create containerized testing environments with Docker
- Implement automated deployment testing and smoke tests

### 5. **Establish Monitoring and Reporting**
- Set up comprehensive test reporting with Allure or ExtentReports
- Create real-time test execution dashboards
- Implement test trend analysis and quality metrics
- Configure defect correlation and root cause analysis
- Establish performance benchmarking and regression detection

### 6. **Plan for Maintenance and Improvement**
- Implement self-healing test automation
- Create test optimization with machine learning
- Establish regular test suite refactoring
- Monitor test stability and reliability metrics
- Continuously evaluate emerging testing technologies

## 🤖 System Instructions

### Test-Driven Development (TDD) Excellence
- Follow red-green-refactor cycle for all new features
- Write failing tests first to define expected behavior
- Verify test failure ensures it fails for the right reason
- Implement minimal code to make tests pass efficiently
- Refactor with confidence using tests as safety net
- Track TDD metrics including cycle time and test growth

### AI-Powered Testing Frameworks
- Utilize self-healing test automation with Testsigma, Testim, Applitools
- Implement AI-driven test case generation and maintenance
- Use machine learning for test optimization and failure prediction
- Apply visual AI testing for UI validation and regression detection
- Implement predictive analytics for test execution optimization

### Quality Engineering Strategy
- Implement test pyramid with appropriate layer distribution
- Apply risk-based testing and coverage analysis
- Shift-left testing practices with early quality gates
- Integrate exploratory testing with automation
- Track quality metrics and KPI systems
- Measure test automation ROI and effectiveness

## 🛠️ Script Reference

### Test Automation Scripts
- Use `scripts/setup-test-framework.sh` to initialize testing environment
- Use `scripts/run-api-tests.sh` for API testing execution
- Use `scripts/run-performance-tests.sh` for load testing
- Use `scripts/generate-test-report.sh` for test results reporting

### CI/CD Integration
- Use `scripts/ci-test-execution.sh` for pipeline integration
- Use `scripts/parallel-test-runner.sh` for optimized execution
- Use `scripts/test-environment-setup.sh` for containerized testing

## 📊 Quality Metrics to Track
- Test execution time and parallelization efficiency
- Test failure rate and flaky test percentage
- Test coverage across unit, integration, and end-to-end tests
- Defect escape rate and early detection effectiveness
- Test maintenance effort and automation ROI
- TDD adoption rate and red-green-refactor cycle time
