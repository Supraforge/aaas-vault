---
name: orchestrating-tdd-workflows
description: >-
  Orchestrates comprehensive Test-Driven Development workflows with strict
  red-green-refactor discipline, multi-agent coordination, and modern testing
  practices
version: 1.0.0
dependencies:
  - python3
  - pytest
  - coverage
  - git
  - jq
compatibility: 'agent-zero, claude-code, cursor'
---

# TDD Workflows Orchestration

## 🎯 Triggers
- "Implement TDD for this feature"
- "Set up red-green-refactor workflow"
- "Orchestrate multi-agent TDD coordination"
- "Establish TDD discipline across team"
- "Create comprehensive test-driven development workflow"

## ⚡ Quick Start (Self-Check)
Before running complex TDD workflows, verify readiness:
- [ ] Run `bash ~/.gemini/skills/orchestrating-tdd-workflows/test.sh` to check dependencies
- [ ] Ensure test frameworks are properly configured
- [ ] Verify git repository is initialized for version control

## 📋 Workflow

### 1. **Ingest**: Analyze Requirements and Establish TDD Foundation
- Analyze project requirements and define acceptance criteria
- Identify edge cases and create comprehensive test scenarios
- Design test architecture with proper structure, fixtures, and mocks
- Establish coverage thresholds (80% line, 75% branch, 100% critical path)

### 2. **Execute**: Orchestrate Red-Green-Refactor Cycles
#### **RED Phase** (Test Specification)
- Write failing tests that define desired behavior
- Ensure tests are specific, isolated, and meaningful
- Verify tests fail for the right reasons
- Document test scenarios and acceptance criteria

#### **GREEN Phase** (Implementation)
- Write minimal implementation to make tests pass
- Focus on functionality, not perfection
- Verify all tests pass
- Maintain test execution speed (< 5 seconds for unit tests)

#### **REFACTOR Phase** (Improvement)
- Improve code structure while keeping tests green
- Apply Clean Code principles
- Reduce complexity (cyclomatic complexity ≤ 10)
- Eliminate duplication and improve readability

### 3. **Verify**: Validate TDD Compliance and Quality
- Run comprehensive test suites
- Generate coverage reports
- Validate against coverage thresholds
- Check code quality metrics
- Ensure zero defects in covered code

## 🤖 System Instructions

### TDD Discipline Enforcement
- **Strict Phase Order**: Always follow RED → GREEN → REFACTOR sequence
- **Test-First Mandate**: Never write implementation before tests
- **Incremental Progress**: Small, focused test-implementation cycles
- **Refactoring Requirement**: Refactoring is NOT optional

### Multi-Agent Coordination
- Delegate specialized testing tasks to appropriate agents
- Coordinate unit, integration, and E2E testing workflows
- Synchronize test suite evolution across development streams
- Manage parallel test development and execution

### Quality Gates
- **Coverage Thresholds**: Minimum 80% line coverage, 75% branch coverage
- **Complexity Limits**: Cyclomatic complexity ≤ 10, method length ≤ 20 lines
- **Performance Requirements**: Test execution < 5 seconds for unit tests
- **Independence**: Tests must be isolated and independent

### Failure Recovery Protocol
1. **STOP** immediately if TDD discipline is broken
2. Identify which phase was violated
3. Rollback to last valid state
4. Resume from correct phase
5. Document lesson learned

## 🛠️ Script Reference

### Core TDD Commands
- **tdd-red**: Execute RED phase - write failing tests
- **tdd-green**: Execute GREEN phase - implement to pass tests
- **tdd-refactor**: Execute REFACTOR phase - improve code quality
- **tdd-cycle**: Complete RED-GREEN-REFACTOR cycle

### Agent Orchestration
- **tdd-orchestrator**: Master TDD orchestrator for workflow coordination
- **code-reviewer**: Specialized agent for test code quality review

### Validation Tools
- **Coverage Analysis**: Line, branch, function, statement coverage
- **Complexity Checking**: Cyclomatic complexity, method/class length
- **Test Performance**: Execution time monitoring
- **Quality Metrics**: Defect escape rate, refactoring frequency

## 📊 TDD Metrics Tracking

Track and report key metrics:
- **Time Distribution**: Time spent in RED/GREEN/REFACTOR phases
- **Cycle Efficiency**: Number of test-implementation cycles
- **Coverage Progression**: Coverage improvement over time
- **Quality Indicators**: Defect escape rate, refactoring frequency
- **Velocity Impact**: Development velocity with TDD discipline

## ⚠️ Anti-Patterns to Avoid

- ❌ Writing implementation before tests
- ❌ Writing tests that already pass
- ❌ Skipping the refactor phase
- ❌ Writing multiple features without tests
- ❌ Modifying tests to make them pass
- ❌ Ignoring failing tests
- ❌ Writing tests after implementation

## ✅ Success Criteria

- ✅ 100% of code written test-first
- ✅ All tests pass continuously
- ✅ Coverage exceeds defined thresholds
- ✅ Code complexity within acceptable limits
- ✅ Zero defects in covered code
- ✅ Clear, comprehensive test documentation
- ✅ Fast test execution (< 5 seconds for unit tests)

## 🔄 Continuous Improvement

- Regularly review and optimize TDD workflows
- Incorporate feedback from development teams
- Adapt to project-specific needs and constraints
- Stay current with modern testing practices and tools
- Scale TDD practices across teams and organizational boundaries
