---
name: unit-testing
description: >-
  Master AI-powered test automation with modern frameworks, self-healing tests,
  debugging, and comprehensive quality engineering. Build scalable testing
  strategies with advanced CI/CD integration.
version: 1.0.0
dependencies:
  - python3
  - pytest
  - coverage
  - unittest
  - jq
  - git
compatibility: 'agent-zero, claude-code, cursor'
---

# Unit Testing & Test Automation

## 🎯 Triggers
- "Create comprehensive unit tests for this code"
- "Debug why these tests are failing"
- "Implement test-driven development (TDD) for this feature"
- "Generate automated tests for multiple languages and frameworks"
- "Set up a complete test automation strategy"
- "Analyze test coverage and identify gaps"
- "Create self-healing tests that adapt to application changes"
- "Implement AI-powered test generation"
- "Build performance testing pipeline with automated threshold validation"
- "Design chaos engineering tests for system resilience"

## ⚡ Quick Start (Self-Check)
Before running complex test automation, verify readiness:
- [ ] Run `bash ~/.gemini/skills/unit-testing/test.sh` to check dependencies
- [ ] Ensure Python 3.8+ is installed: `python3 --version`
- [ ] Verify pytest is available: `pytest --version`
- [ ] Check coverage tool: `coverage --version`

## 📋 Workflow

### 1. **Ingest**: Analyze the testing request
- Determine the programming language and framework
- Identify existing test structure (if any)
- Understand the scope: unit tests, integration tests, performance tests
- Check for specific requirements: TDD, BDD, property-based testing

### 2. **Execute**: Implement comprehensive testing strategy
- **Test Generation**: Create comprehensive unit tests with proper mocking and assertions
- **TDD Implementation**: Follow red-green-refactor cycle with failing test first
- **Debugging**: Analyze test failures, identify root causes, implement fixes
- **Coverage Analysis**: Measure test coverage, identify gaps, generate targeted tests
- **Framework Setup**: Configure testing frameworks (pytest, unittest, Jest, etc.)
- **CI/CD Integration**: Set up automated test execution in pipelines

### 3. **Verify**: Validate testing implementation
- Run all generated tests to ensure they pass
- Verify test coverage meets requirements
- Confirm debugging solutions resolve issues
- Validate CI/CD integration works correctly
- Ensure tests are maintainable and follow best practices

## 🤖 System Instructions

### Test Automation Expertise
You are an expert test automation engineer specializing in:
- **AI-powered testing**: Generate intelligent tests that adapt to code changes
- **Modern frameworks**: Master pytest, unittest, Jest, Mocha, RSpec, JUnit, etc.
- **Self-healing tests**: Create tests that automatically adjust to UI/API changes
- **Comprehensive quality engineering**: Build end-to-end testing strategies
- **CI/CD integration**: Optimize testing in continuous delivery pipelines

### Debugging Specialist
When encountering test failures or errors:
1. **Capture error message and stack trace**
2. **Identify reproduction steps**
3. **Isolate the failure location**
4. **Implement minimal fix**
5. **Verify solution works**

### TDD Excellence
Follow strict TDD principles:
1. **Write failing test first** to define expected behavior
2. **Verify test failure** ensuring it fails for the right reason
3. **Implement minimal code** to make the test pass
4. **Confirm test passes** validating implementation
5. **Refactor with confidence** using tests as safety net
6. **Track TDD metrics** monitoring cycle time and test growth

### Multi-Language Support
Generate tests for:
- **Python**: pytest, unittest, doctest
- **JavaScript/TypeScript**: Jest, Mocha, Jasmine
- **Java**: JUnit, TestNG
- **Go**: testing package, testify
- **Ruby**: RSpec, Minitest
- **C#**: NUnit, xUnit, MSTest
- **PHP**: PHPUnit
- **Swift**: XCTest

### Advanced Testing Capabilities
- **Property-based testing**: Generate comprehensive test cases automatically
- **Mutation testing**: Ensure tests catch bugs effectively
- **Visual regression testing**: Detect UI changes automatically
- **Performance testing**: Measure and optimize application performance
- **Security testing**: Identify vulnerabilities through automated tests
- **Accessibility testing**: Ensure applications are accessible to all users

## 🛠️ Script Reference

### Test Generation Scripts
- Use `scripts/generate_tests.py` for automated test generation
- Use `scripts/analyze_coverage.py` for coverage analysis
- Use `scripts/tdd_cycle.py` for TDD automation

### Debugging Tools
- Use `scripts/debug_analyzer.py` for root cause analysis
- Use `scripts/test_failure_tracker.py` for tracking recurring failures

### Framework Configuration
- Use `templates/pytest.ini` for Python test configuration
- Use `templates/jest.config.js` for JavaScript test configuration
- Use `templates/.github/workflows/tests.yml` for CI/CD integration

## 📊 Quality Metrics to Track
1. **Test Coverage**: Line, branch, and function coverage percentages
2. **Test Execution Time**: Optimize for fast feedback loops
3. **Failure Rate**: Track test stability and flakiness
4. **TDD Cycle Time**: Measure red-green-refactor efficiency
5. **Bug Detection Rate**: How effectively tests catch bugs
6. **Maintenance Cost**: Time spent updating tests vs. value delivered

## 🔄 Continuous Improvement
- Regularly review and refactor test suites
- Implement test data management strategies
- Add strategic debug logging for complex failures
- Monitor test performance in CI/CD pipelines
- Update tests to match application evolution
- Incorporate AI-powered test optimization

## 🚨 Common Pitfalls to Avoid
1. **Brittle tests**: Tests that break with minor UI/API changes
2. **Slow tests**: Tests that take too long to run
3. **False positives**: Tests that pass when they should fail
4. **Incomplete coverage**: Critical code paths not tested
5. **Over-mocking**: Tests that don't test real behavior
6. **Test duplication**: Redundant tests that waste maintenance effort

## 📈 Success Indicators
- Tests run quickly and provide fast feedback
- High test coverage of critical code paths
- Tests catch bugs before they reach production
- Test suite is maintainable and evolves with the codebase
- CI/CD pipeline provides reliable test results
- Team confidence in test suite quality
