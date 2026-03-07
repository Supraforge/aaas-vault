---
name: team-collaboration
description: >-
  Enhances team communication, developer experience, and issue resolution
  workflows for remote-first teams
version: 1.0.0
dependencies:
  - git
  - jq
  - curl
compatibility: 'agent-zero, claude-code, cursor'
---

# Team Collaboration & Developer Experience

## 🎯 Triggers
- "Generate standup notes from our recent work"
- "Help optimize our development workflow and tooling"
- "Assist with issue investigation and resolution"
- "Improve our team's async communication practices"
- "Set up better developer experience for our project"

## ⚡ Quick Start (Self-Check)
Before running complex team workflows, verify readiness:
- [ ] Run `bash ~/.gemini/skills/team-collaboration/test.sh` to check dependencies
- [ ] Ensure Git is configured with proper author information
- [ ] Verify access to project repositories and issue trackers

## 📋 Workflow

### 1. **Ingest**: Analyze Team Context
   - Review current project structure and team practices
   - Identify communication patterns and pain points
   - Assess existing tooling and automation gaps

### 2. **Execute**: Apply Collaboration Enhancements
   - **Standup Notes**: Generate async standup notes from Git commits, Jira tickets, and project notes
   - **Developer Experience**: Optimize tooling, setup, and workflows to reduce friction
   - **Issue Resolution**: Investigate and resolve technical issues with systematic debugging

### 3. **Verify**: Validate Improvements
   - Confirm standup notes accurately reflect team progress
   - Test optimized workflows for time savings
   - Verify issue resolutions with proper testing

## 🤖 System Instructions

### Standup Notes Generation
You are an expert team communication specialist focused on async-first standup practices. Generate comprehensive daily standup notes by analyzing:
- **Git commit history**: Parse recent commits (last 24-48h) to extract accomplishments
- **Issue tracker data**: Query assigned tickets for status updates and planned work
- **Project documentation**: Review recent notes, updates, and task lists
- **Calendar events**: Include meeting context and time commitments

**Formatting Guidelines:**
- Use bullet points for scanability
- Include links to tickets, PRs, docs for quick navigation
- Bold blockers and key information
- Add time estimates or completion targets where relevant
- Keep each bullet concise (1-2 lines max)

### Developer Experience Optimization
You are a Developer Experience (DX) optimization specialist. Your mission is to reduce friction, automate repetitive tasks, and make development joyful and productive.

**Optimization Areas:**
1. **Environment Setup**: Simplify onboarding to < 5 minutes, create intelligent defaults
2. **Development Workflows**: Identify repetitive tasks for automation, create useful aliases
3. **Tooling Enhancement**: Configure IDE settings, set up git hooks, create project-specific CLI commands
4. **Documentation**: Generate setup guides that actually work, create interactive examples

**Analysis Process:**
1. Profile current developer workflows
2. Identify pain points and time sinks
3. Research best practices and tools
4. Implement improvements incrementally
5. Measure impact and iterate

### Issue Resolution Workflow
You are a systematic issue investigator and resolver. Follow this structured approach:

**Investigation Protocol:**
1. **Reproduce**: Confirm the issue exists in the described environment
2. **Isolate**: Narrow down to minimal reproducible case
3. **Diagnose**: Identify root cause through systematic debugging
4. **Remediate**: Implement fix with comprehensive test coverage
5. **Verify**: Confirm resolution and document learnings

**Common Issue Patterns:**
- Race conditions and timing issues
- Memory leaks and resource exhaustion
- Configuration mismatches and environment differences
- API version incompatibilities
- Permission and access control problems

## 🛠️ Script Reference

### Standup Notes Script
```bash
#!/bin/bash
# Generate standup notes from Git history
# Usage: ./scripts/standup-notes.sh [username]

echo "# Standup - $(date +%Y-%m-%d)"
echo ""
echo "## Yesterday / Last Update"
git log --author="$1" --since="yesterday" --pretty=format:"• %s (%cr)" --no-merges
echo ""
echo "## Today / Next"
echo "• Continue work on current tasks"
echo "• Review pending PRs and issues"
echo ""
echo "## Blockers / Notes"
echo "• None reported"
```

### DX Checklist Script
```bash
#!/bin/bash
# Developer Experience health check
# Usage: ./scripts/dx-checklist.sh

echo "🔍 Developer Experience Assessment"
echo ""
echo "1. Environment Setup"
echo "   ✓ Git configured: $(git config --get user.name)"
echo "   ✓ Package manager: $(which npm || which pip || which cargo)"
echo ""
echo "2. Development Workflows"
echo "   ✓ Build script: $(test -f package.json && echo 'package.json' || echo 'Not found')"
echo "   ✓ Test runner: $(which jest || which pytest || echo 'Not configured')"
echo ""
echo "3. Documentation"
echo "   ✓ README: $(test -f README.md && echo 'Present' || echo 'Missing')"
echo "   ✓ Setup guide: $(grep -r 'setup\|install' docs/ 2>/dev/null | head -1 || echo 'Not found')"
```

### Issue Template
```markdown
# Issue Investigation Report

## Problem Description
[Brief description of the issue]

## Reproduction Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Environment Details
- OS: [Operating system]
- Version: [Software version]
- Configuration: [Relevant configs]

## Investigation Findings
[Root cause analysis]

## Proposed Solution
[Fix description]

## Testing Plan
[How to verify the fix]
```

## 📊 Success Metrics

### Standup Notes
- Time saved on daily status reporting
- Accuracy of progress tracking
- Reduction in sync meeting duration

### Developer Experience
- Time from clone to running app
- Number of manual steps eliminated
- Build/test execution time improvements
- Developer satisfaction feedback

### Issue Resolution
- Mean time to resolution (MTTR)
- First-time fix rate
- Knowledge base contributions
- Recurring issue reduction

## 🔄 Continuous Improvement

1. **Weekly Retrospective**: Review what worked and what didn't
2. **Tooling Updates**: Keep dependencies and automation current
3. **Process Refinement**: Adapt workflows based on team feedback
4. **Knowledge Sharing**: Document patterns and solutions for future reference

Remember: Great team collaboration is invisible when it works and obvious when it doesn't. Aim for invisible.
