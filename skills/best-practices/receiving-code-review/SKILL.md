---
name: receiving-code-review
description: >-
  Use when receiving code review feedback, before implementing suggestions,
  especially if feedback seems unclear or technically questionable - requires
  technical rigor and verification, not performative agreement or blind
  implementation
version: 1.0.0
dependencies:
  - bash
compatibility: 'agent-zero, claude-code, cursor'
---

# Code Review Reception

## Overview

Code review requires technical evaluation, not emotional performance.

**Core principle:** Verify before implementing. Ask before assuming. Technical correctness over social comfort.

## The Response Pattern

```
WHEN receiving code review feedback:

1. READ: Complete feedback without reacting
2. UNDERSTAND: Restate requirement in own words (or ask)
3. VERIFY: Check technical correctness
4. DECIDE: Accept, reject, or ask for clarification
5. IMPLEMENT: Only after steps 1-4
```

## Step 1: Read Without Reacting

**Don't:**
- Immediately agree
- Immediately disagree
- Get defensive
- Assume intent

**Do:**
- Read all feedback
- Note unclear points
- Identify technical claims
- Separate style from substance

## Step 2: Understand (Restate or Ask)

**Restate in your own words:**

```
Reviewer: "This seems inefficient"
You: "You're saying the O(n²) algorithm could be O(n log n)?"
```

**If unclear, ask:**

```
Reviewer: "This could be better"
You: "What specific improvement do you suggest?"
```

**Never:** "I don't understand" (vague)
**Always:** "Which part specifically?" or "Can you give an example?"

## Step 3: Verify Technical Correctness

**Check claims:**
- Is the performance claim true? (benchmark)
- Is the security concern valid? (analysis)
- Does the alternative actually work? (test)
- Is this a preference vs requirement?

**Tools:**
- Run benchmarks
- Check documentation
- Test alternatives
- Research best practices

## Step 4: Decide (Accept/Reject/Clarify)

**Accept when:**
- Technically correct
- Improves code
- Aligns with requirements

**Reject when:**
- Technically incorrect
- Makes code worse
- Conflicts with requirements

**Ask for clarification when:**
- Unclear what's being asked
- Need more context
- Seems contradictory

## Step 5: Implement (Only After Verification)

**If accepting:**
- Make the change
- Explain why in response
- Reference verification

**If rejecting:**
- Explain technical reasons
- Provide evidence
- Suggest alternatives

**If asking:**
- Get clarification first
- Then return to step 3

## Common Scenarios

### Scenario 1: Vague Feedback

**Reviewer:** "This could be cleaner"

**Bad response:** "OK, I'll clean it up" (performative)
**Good response:** "What specifically should be cleaner? The error handling, the variable names, or the structure?"

### Scenario 2: Questionable Technical Claim

**Reviewer:** "This will be slow with large data"

**Bad response:** "I'll optimize it" (blind)
**Good response:** "Let me benchmark with large dataset. Current complexity is O(n). What size data are you concerned about?"

### Scenario 3: Style Preference

**Reviewer:** "I prefer early returns"

**Bad response:** "Sure, I'll change it" (performative)
**Good response:** "The project style guide allows both. Is there a technical reason to prefer early returns here?"

### Scenario 4: Missing Context

**Reviewer:** "This doesn't handle edge case X"

**Bad response:** "I'll add it" (blind)
**Good response:** "Edge case X shouldn't happen because of constraint Y. Should we still handle it defensively?"

## Red Flags

**Performative agreement:** Changing code without understanding why
**Defensive rejection:** Rejecting feedback without verification
**Vague questions:** "I don't understand" instead of specific questions
**Emotional language:** "I feel", "I think", "I believe" in technical discussion

## Technical Verification Examples

### Performance Claim

**Reviewer:** "This loop is O(n²)"
**Verification:**
```python
import timeit
# Test with increasing n
# Plot results
# Compare to O(n log n) alternative
```

### Security Claim

**Reviewer:** "This could be SQL injection"
**Verification:**
- Check if inputs are sanitized
- Check ORM usage
- Test with malicious input

### Correctness Claim

**Reviewer:** "This algorithm is wrong for case X"
**Verification:**
- Write test for case X
- Run existing tests
- Check against specification

## Response Templates

### Asking for Clarification

```
"Can you clarify what you mean by [vague term]?"
"Which part specifically needs improvement?"
"Can you give an example of how this would look?"
```

### Pushing Back (Technical Reasons)

```
"I tested this and found [evidence]."
"The documentation says [reference]."
"This would break [requirement] because [reason]."
```

### Accepting with Explanation

```
"You're right about [issue]. I'll fix it by [change]."
"Good catch. I verified [claim] and will update."
```

## Real Example

**Reviewer:** "Use Promise.all instead of sequential awaits"

**Response:**
1. Read: They want parallelization
2. Understand: "You're suggesting parallel execution of these 3 API calls?"
3. Verify: Check if calls are independent (yes), benchmark sequential vs parallel
4. Decide: Accept - technically correct, improves performance
5. Implement: Change to Promise.all, show 40% speedup in response

## Key Benefits

1. **Technical rigor** - Decisions based on evidence
2. **Learning** - Understand why changes are needed
3. **Quality** - Only make improvements that actually help
4. **Respect** - Treat feedback as technical, not personal

## Integration

**Called by:**
- **requesting-code-review** - After receiving feedback
- **finishing-a-development-branch** - During PR review

**Pairs with:**
- **systematic-debugging** - For technical verification
- **test-driven-development** - For correctness checks
