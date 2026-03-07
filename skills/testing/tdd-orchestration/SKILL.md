---
name: tdd-orchestration
description: >-
  Orchestrates comprehensive test-driven development workflows, enforces
  red-green-refactor discipline, coordinates multi-agent testing, and manages
  TDD metrics across development teams
version: 1.0.0
dependencies:
  - python3
  - git
  - pytest
  - jest
  - mocha
  - docker
  - nodejs
  - jq
  - yq
  - curl
  - make
  - npm
  - pip
compatibility: 'agent-zero, claude-code, cursor'
---

# TDD Orchestration

## 🎯 Triggers
- "Implement TDD for our new project"
- "Orchestrate test-driven development across multiple teams"
- "Enforce red-green-refactor discipline in our workflow"
- "Coordinate multi-agent testing workflows"
- "Set up TDD metrics and compliance monitoring"
- "Migrate legacy code to TDD with safety nets"
- "Design property-based testing strategies"
- "Implement mutation testing pipelines"

## ⚡ Quick Start (Self-Check)
Before orchestrating TDD workflows, verify readiness:
- [ ] Run `bash ~/.gemini/skills/tdd-orchestration/test.sh` to check dependencies
- [ ] Ensure git repository is initialized and accessible
- [ ] Verify testing frameworks are installed (pytest, jest, mocha, etc.)
- [ ] Check CI/CD pipeline access if available

## 📋 Workflow

### 1. **Assess TDD Readiness**
- Analyze current development practices and test coverage
- Evaluate team TDD maturity and existing test infrastructure
- Identify gaps in testing discipline and tooling
- Assess codebase complexity and refactoring needs

### 2. **Establish TDD Discipline**
- Implement red-green-refactor cycle enforcement
- Set up test-first development practices
- Create automated compliance checking mechanisms
- Establish refactoring safety nets and regression prevention

### 3. **Orchestrate Multi-Agent Workflows**
- Coordinate specialized testing agents (unit, integration, E2E)
- Delegate parallel test development tasks
- Synchronize test suite evolution across development streams
- Manage cross-team TDD practice alignment

### 4. **Implement Comprehensive Metrics**
- Track TDD cycle times and feedback loops
- Monitor test coverage and quality metrics
- Measure refactoring safety and regression rates
- Report on TDD compliance and team productivity

### 5. **Coordinate Refactoring Efforts**
- Plan safe refactoring with comprehensive test safety nets
- Coordinate legacy code modernization with TDD practices
- Implement automated refactoring tools and techniques
- Ensure clean code principles in test and production code

### 6. **Optimize Test Execution**
- Parallelize test execution for rapid feedback
- Implement test selection and prioritization
- Optimize test environment setup and teardown
- Manage test data and fixture lifecycle

### 7. **Scale TDD Practices**
- Extend TDD governance across organizational boundaries
- Implement automated quality gate enforcement
- Create TDD training and knowledge sharing programs
- Establish continuous improvement feedback loops

## 🤖 System Instructions

### TDD Orchestration Principles
1. **Test-First Discipline**: Always write tests before implementation
2. **Red-Green-Refactor Cycle**: Strict adherence to the TDD rhythm
3. **Safety First**: Comprehensive test safety nets before refactoring
4. **Rapid Feedback**: Optimize for shortest possible feedback loops
5. **Continuous Improvement**: Regular TDD practice refinement

### Multi-Agent Coordination Rules
- Delegate specialized testing tasks to appropriate agents
- Maintain clear communication channels between agents
- Synchronize test suite evolution and dependency management
- Ensure consistent TDD practices across all agents

### Metrics and Compliance
- Track key TDD metrics: cycle time, test coverage, defect escape rate
- Implement automated compliance checking and reporting
- Use metrics for continuous improvement, not punishment
- Share metrics transparently across teams

## 🛠️ Script Reference

### Core Scripts
- `scripts/tdd-setup.sh` - Initializes TDD environment and tooling
- `scripts/test-coordination.sh` - Coordinates multi-agent test execution
- `scripts/metrics-collection.sh` - Collects and reports TDD metrics
- `scripts/compliance-check.sh` - Verifies TDD discipline compliance

### Template Files
- `templates/tdd-workflow-template.md` - Standard TDD workflow documentation
- `templates/test-plan-template.md` - Comprehensive test planning template
- `templates/metrics-dashboard-template.json` - TDD metrics dashboard configuration
- `templates/agent-coordination-protocol.md` - Multi-agent coordination guidelines

## 📊 TDD Metrics Dashboard

The skill includes automated metrics collection for:
- **Cycle Time**: Red-to-green and green-to-refactor durations
- **Test Coverage**: Line, branch, and mutation coverage metrics
- **Defect Escape Rate**: Bugs found in production vs. caught by tests
- **Refactoring Safety**: Regression rate after refactoring operations
- **Team Velocity**: Development throughput with TDD practices

## 🔄 Integration Points

### CI/CD Pipeline Integration
- Pre-commit hooks for test-first compliance
- Automated test execution in CI pipelines
- Quality gate enforcement based on TDD metrics
- Deployment blocking for TDD compliance violations

### Development Environment Integration
- IDE plugins for TDD workflow support
- Test runner integration and optimization
- Code review tools with TDD compliance checking
- Pair programming facilitation tools

### Monitoring and Alerting
- Real-time TDD compliance monitoring
- Alerting for TDD practice deviations
- Performance degradation detection in test suites
- Resource utilization optimization for test execution
