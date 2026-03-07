---
name: code-review-excellence
description: >-
  Master effective code review practices to provide constructive feedback, catch
  bugs early, and foster knowledge sharing while maintaining team morale. Use
  when reviewing pull requests, establishing review standards, or mentoring
  developers.
version: 1.0.0
dependencies: []
compatibility: 'agent-zero, claude-code, cursor'
---

# Code Review Excellence

Transform code reviews from gatekeeping to knowledge sharing through constructive feedback, systematic analysis, and collaborative improvement.

## When to Use This Skill

- Reviewing pull requests and code changes
- Establishing code review standards for teams
- Mentoring junior developers through reviews
- Conducting architecture reviews
- Creating review checklists and guidelines
- Improving team collaboration
- Reducing code review cycle time
- Maintaining code quality standards

## Core Principles

### 1. The Review Mindset

**Goals of Code Review:**
- Catch bugs and edge cases
- Ensure code maintainability
- Share knowledge across team
- Enforce coding standards
- Improve design and architecture
- Build team culture

**Not the Goals:**
- Show off knowledge
- Nitpick formatting (use linters)
- Block progress unnecessarily
- Rewrite to your preference

### 2. Effective Feedback

**Good Feedback is:**
- Specific and actionable
- Educational, not judgmental
- Focused on the code, not the person
- Balanced (positive + constructive)
- Timely and relevant

**Bad Feedback is:**
- Vague ("This looks wrong")
- Personal ("You always...")
- Overwhelming (50+ comments)
- Nitpicky (spacing, naming preferences)
- Delayed (days after submission)

### 3. Systematic Review Process

**Before Reviewing:**
1. Understand the PR context and requirements
2. Check if tests exist and pass
3. Review the smallest logical unit first

**During Review:**
1. Look for correctness and edge cases
2. Check for maintainability and readability
3. Verify adherence to team standards
4. Consider security implications
5. Assess performance impact

**After Review:**
1. Provide clear next steps
2. Follow up on requested changes
3. Celebrate merged contributions

## Review Checklist

### ✅ Must-Have Checks

**Functionality:**
- [ ] Code compiles/parses without errors
- [ ] Tests pass and cover new functionality
- [ ] Edge cases are handled
- [ ] No breaking changes to existing APIs

**Security:**
- [ ] No hardcoded secrets
- [ ] Input validation exists where needed
- [ ] No SQL injection/XSS vulnerabilities
- [ ] Authentication/authorization checks

**Performance:**
- [ ] No obvious performance regressions
- [ ] Database queries are optimized
- [ ] Memory usage is reasonable

**Maintainability:**
- [ ] Code follows team conventions
- [ ] Meaningful variable/function names
- [ ] Comments explain "why" not "what"
- [ ] No dead or commented-out code

### 🔍 Nice-to-Have Checks

**Design:**
- [ ] Separation of concerns
- [ ] Appropriate abstractions
- [ ] Single responsibility principle
- [ ] Open/closed principle

**Testing:**
- [ ] Test coverage for critical paths
- [ ] Integration tests where needed
- [ ] Mocking external dependencies

**Documentation:**
- [ ] README updates if needed
- [ ] API documentation updates
- [ ] Configuration changes documented

## Common Anti-Patterns

**The Nitpicker:**
- Comments on formatting that could be automated
- Requests changes for personal preference
- Ignores major issues while focusing on minor ones

**The Ghost Reviewer:**
- Requests changes then disappears
- Doesn't follow up on discussions
- Leaves PR hanging for days

**The Rubber Stamper:**
- Approves without actual review
- "LGTM" with no substance
- Misses critical issues

**The Rewriter:**
- Requests complete rewrites
- Imposes personal coding style
- Doesn't respect original author's approach

## Advanced Techniques

### 1. Pair Reviewing
Review code together with the author to:
- Build shared understanding
- Reduce back-and-forth comments
- Provide immediate feedback
- Teach and learn simultaneously

### 2. Checklist-Driven Reviews
Create team-specific checklists for:
- Security reviews
- Performance-sensitive code
- UI/UX changes
- Database migrations

### 3. Automated First Pass
Use tools to handle:
- Code formatting
- Linting violations
- Simple syntax errors
- Test coverage

### 4. Time-Boxed Reviews
Set limits:
- 15 minutes for small PRs
- 30 minutes for medium PRs
- 60 minutes for large PRs
- Escalate if more time needed

## Language-Specific Considerations

### JavaScript/TypeScript
- Check for proper TypeScript types
- Verify async/await error handling
- Look for memory leaks in event listeners
- Ensure proper module imports/exports

### Python
- Check for proper exception handling
- Verify type hints (if using mypy)
- Look for mutable default arguments
- Ensure proper virtual environment usage

### Go
- Check error handling patterns
- Verify interface implementations
- Look for goroutine leaks
- Ensure proper package organization

### Java
- Check null safety
- Verify exception hierarchy
- Look for resource leaks
- Ensure proper package structure

## Handling Difficult Situations

### When You Disagree
1. **Separate opinion from fact** - "I prefer X" vs "X is wrong"
2. **Provide evidence** - Link to docs, benchmarks, or examples
3. **Defer to team standards** - Reference existing patterns
4. **Escalate if needed** - Involve tech lead or architect

### When Code is Fundamentally Flawed
1. **Be specific** - Point to exact issues
2. **Suggest alternatives** - Provide concrete solutions
3. **Offer to pair** - Help implement fixes
4. **Consider incremental improvement** - Can it be fixed in phases?

### When Review Takes Too Long
1. **Time-box your review** - Set a timer
2. **Prioritize issues** - Blockers vs suggestions
3. **Request smaller PRs** - Suggest breaking it up
4. **Use review tools** - GitHub suggestions, inline comments

## Measuring Review Effectiveness

### Quantitative Metrics
- **Cycle time**: PR open to merge
- **Review depth**: Comments per 100 lines
- **Review coverage**: % of PRs reviewed
- **Feedback quality**: Ratio of actionable to nitpick comments

### Qualitative Metrics
- **Developer satisfaction** with review process
- **Knowledge sharing** observed in team
- **Bug escape rate** to production
- **Code quality trends** over time

## Continuous Improvement

### Regular Retrospectives
Discuss as a team:
- What's working well in our reviews?
- What pain points are we experiencing?
- How can we improve our checklist?
- Are we balancing speed with quality?

### Skill Development
- Pair junior with senior reviewers
- Create review training sessions
- Share exemplary reviews as examples
- Rotate review responsibilities

## Templates

### PR Review Comment Template

```markdown
## Summary
[Brief overview of what was reviewed]

## Strengths
- [What was done well]
- [Good patterns or approaches]

## Required Changes
🔴 [Blocking issue 1]
🔴 [Blocking issue 2]

## Suggestions
💡 [Improvement 1]
💡 [Improvement 2]

## Questions
❓ [Clarification needed on X]
❓ [Alternative approach consideration]

## Verdict
✅ Approve after addressing required changes
```

## Resources

- **references/code-review-best-practices.md**: Comprehensive review guidelines
- **references/common-bugs-checklist.md**: Language-specific bugs to watch for
- **references/security-review-guide.md**: Security-focused review checklist
- **assets/pr-review-template.md**: Standard review comment template
- **assets/review-checklist.md**: Quick reference checklist
- **scripts/pr-analyzer.py**: Analyze PR complexity and suggest reviewers
