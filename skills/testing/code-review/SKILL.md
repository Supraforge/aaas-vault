---
name: code-review
description: >-
  Performs comprehensive AI-powered code analysis, security vulnerability
  scanning, performance optimization, and production reliability assessment
  using modern static analysis tools and best practices
version: 1.0.0
dependencies:
  - python3
  - nodejs
  - git
  - jq
  - yq
  - curl
  - docker
  - npm
  - pip
  - sonarqube-scanner
  - semgrep
  - bandit
  - snyk
  - npm-audit
  - pip-audit
  - shellcheck
  - hadolint
  - checkov
  - trivy
compatibility: 'agent-zero, claude-code, cursor'
---

# AI-Powered Code Review

## 🎯 Triggers
- "Review this code for security vulnerabilities"
- "Analyze this pull request for code quality issues"
- "Perform comprehensive code review with static analysis"
- "Check this codebase for performance bottlenecks"
- "Assess production readiness of this deployment configuration"
- "Scan for security compliance violations (SOC2, PCI DSS, GDPR)"
- "Evaluate code maintainability and technical debt"

## ⚡ Quick Start (Self-Check)
- [ ] Run `bash ~/.gemini/skills/code-review/test.sh` to verify all analysis tools are available
- [ ] Configure API keys for commercial tools (Snyk, SonarQube, etc.) if needed
- [ ] Set up project-specific analysis rules in `templates/analysis-rules/`

## 📋 Workflow

### 1. **Context Analysis**
- Identify codebase type (web, mobile, backend, infrastructure)
- Determine programming languages and frameworks used
- Review project structure and build configuration
- Identify critical components and security boundaries
- Assess compliance requirements (SOC2, PCI DSS, HIPAA, GDPR)

### 2. **Automated Tool Execution**
- Run language-specific static analysis tools
- Execute security vulnerability scanners
- Perform dependency vulnerability assessment
- Conduct license compliance checking
- Generate code quality metrics and technical debt reports

### 3. **AI-Powered Analysis**
- Integrate with AI review tools (GitHub Copilot, CodeWhisperer, etc.)
- Apply natural language pattern matching for custom rules
- Perform context-aware code smell detection
- Generate intelligent suggestions for improvements
- Create automated pull request comments

### 4. **Manual Expert Review**
- Analyze business logic and architectural decisions
- Review error handling and resilience patterns
- Assess performance implications and scalability
- Evaluate security controls and access management
- Check configuration management and secrets handling

### 5. **Reporting and Recommendations**
- Generate structured feedback by severity and priority
- Provide specific code examples and alternatives
- Create remediation plans with estimated effort
- Document decisions and rationale
- Follow up on implementation progress

## 🤖 System Instructions

### Review Priorities
1. **Security First**: Always prioritize security vulnerabilities over code style issues
2. **Production Impact**: Focus on issues affecting production reliability and performance
3. **Compliance Requirements**: Ensure regulatory and compliance standards are met
4. **Maintainability**: Promote clean code practices and reduce technical debt
5. **Team Standards**: Align with team-specific coding conventions and patterns

### Tool Integration Strategy
- Use open-source tools for initial scanning
- Integrate commercial tools for enterprise-grade analysis
- Combine multiple tools for comprehensive coverage
- Customize rulesets for project-specific requirements
- Automate repetitive analysis tasks

### Response Standards
- **Critical Issues**: Must-fix vulnerabilities with immediate impact
- **High Priority**: Important improvements with significant benefits
- **Medium Priority**: Recommended changes for long-term maintainability
- **Low Priority**: Optional improvements and style suggestions
- **Informational**: Observations without required action

## 🛠️ Tool Reference

### Static Analysis Tools
- **SonarQube**: Comprehensive code quality and security analysis
- **CodeQL**: Semantic code analysis for security vulnerabilities
- **Semgrep**: Fast, customizable static analysis
- **Bandit**: Python security linter
- **ESLint/TSLint**: JavaScript/TypeScript code quality
- **Checkstyle**: Java code style enforcement
- **RuboCop**: Ruby code quality analyzer

### Security Scanners
- **Snyk**: Dependency vulnerability scanning
- **Trivy**: Container and filesystem vulnerability scanner
- **Checkov**: Infrastructure as Code security scanning
- **Hadolint**: Dockerfile linter
- **npm audit**: Node.js dependency vulnerabilities
- **pip-audit**: Python package vulnerabilities
- **OWASP Dependency-Check**: Comprehensive dependency analysis

### Performance Analysis
- **Profiling Tools**: Language-specific profilers (cProfile, JProfiler, etc.)
- **Complexity Analyzers**: Cyclomatic complexity and cognitive load
- **Memory Analyzers**: Heap analysis and memory leak detection
- **Network Analysis**: API performance and latency assessment

### AI-Powered Tools
- **GitHub Copilot**: AI-assisted code review and suggestions
- **Amazon CodeWhisperer**: Security-focused AI code analysis
- **Tabnine**: AI code completion and review
- **Codeium**: Free AI code assistant with review capabilities

## 📊 Metrics and Reporting

### Quality Metrics
- **Code Coverage**: Test coverage percentage by component
- **Technical Debt**: Estimated remediation effort in hours
- **Security Score**: Vulnerability severity weighted score
- **Performance Score**: Response time and resource utilization metrics
- **Maintainability Index**: Code complexity and documentation quality

### Compliance Metrics
- **Regulatory Compliance**: Percentage of requirements met
- **Security Controls**: Implementation status of security controls
- **Access Management**: Proper authentication and authorization coverage
- **Data Protection**: Encryption and data handling compliance

### Team Performance Metrics
- **Review Velocity**: Time to complete code reviews
- **Defect Detection Rate**: Bugs caught before production
- **Knowledge Sharing**: Cross-team learning and best practice adoption
- **Continuous Improvement**: Trend analysis of code quality over time

## 🔄 Integration Points

### CI/CD Pipeline Integration
- Pre-commit hooks for automated code analysis
- Pull request validation with quality gates
- Automated security scanning in build pipelines
- Deployment blocking for critical vulnerabilities
- Quality metrics collection and reporting

### Development Environment Integration
- IDE plugins for real-time code analysis
- Editor configuration for consistent coding standards
- Local pre-commit validation scripts
- Automated test generation for identified issues
- Code review checklist integration

### Team Collaboration Integration
- Pull request template with review checklist
- Automated comment generation for common issues
- Knowledge base of team-specific patterns
- Training materials based on review findings
- Retrospective analysis of review effectiveness

## 📁 Templates and Scripts

### Available Templates
- `templates/security-review-checklist.md` - Comprehensive security assessment checklist
- `templates/code-quality-rules.yaml` - Customizable code quality rules
- `templates/compliance-requirements.md` - Regulatory compliance checklist
- `templates/performance-review-template.md` - Performance analysis framework
- `templates/report-template.md` - Standardized review report format

### Available Scripts
- `scripts/run-security-scan.sh` - Automated security vulnerability scanning
- `scripts/generate-code-metrics.py` - Code quality metrics generation
- `scripts/analyze-dependencies.sh` - Dependency vulnerability assessment
- `scripts/create-review-report.py` - Automated review report generation
- `scripts/integrate-with-ci.sh` - CI/CD pipeline integration setup
