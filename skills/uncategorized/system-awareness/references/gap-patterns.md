# Gap Patterns - Recognizing Capability Needs

This document helps identify when the system is encountering a capability gap that should be logged.

## Pattern Recognition

### Pattern 1: Direct Inability Statement
**Signal:** Claude explicitly states it cannot do something

**Examples:**
- "I don't have a skill for analyzing ECG images"
- "This system doesn't support audio transcription"
- "I cannot access real-time stock prices"

**Action:** Log immediately with the exact capability missing

---

### Pattern 2: Manual Workaround Required
**Signal:** User has to do something manually that should be automated

**Examples:**
- "Let me manually extract this data and paste it..."
- "You'll need to download this yourself and then..."
- "Can you copy the text from the PDF first?"

**Action:** Log the automation opportunity

---

### Pattern 3: External Tool Redirect
**Signal:** Pointing user to external tools/services

**Examples:**
- "You'll need to use Canva for this"
- "Try using [external service] for that"
- "That would require a specialized tool like..."

**Action:** Log if the capability could reasonably be built internally

---

### Pattern 4: Repeated Similar Requests
**Signal:** Same type of request appears multiple times

**Examples:**
- 3rd request for "ECG interpretation" this week
- Multiple users asking about "podcast transcription"
- Recurring need for "competitor analysis"

**Action:** Log with frequency indicator; high-priority gap

---

### Pattern 5: Wishful Thinking
**Signal:** User expresses desire for capability

**Examples:**
- "I wish the system could automatically..."
- "It would be great if we could..."
- "Can you imagine if this could...?"

**Action:** Log as user-requested feature

---

### Pattern 6: Workflow Interruption
**Signal:** User has to leave the system mid-task

**Examples:**
- "I'll need to do this in Excel and come back"
- "Let me check this in another tool"
- "I have to switch to [other app] for this step"

**Action:** Log the workflow continuity gap

---

### Pattern 7: Approximation or Workaround
**Signal:** Providing an imperfect solution

**Examples:**
- "I can approximate this by..."
- "A workaround would be to..."
- "While I can't do X directly, I can do Y..."

**Action:** Log the ideal capability vs. the workaround

---

### Pattern 8: Feature Comparison Gap
**Signal:** Comparing to competitor or desired state

**Examples:**
- "ChatGPT can do this but..."
- "In [other tool], you can..."
- "The ideal would be..."

**Action:** Log the competitive gap

---

## Gap Categories

### Content Creation Gaps
- New content formats (podcasts, video scripts, courses)
- New platforms (TikTok, LinkedIn, Substack)
- New voices or styles

### Research Gaps
- New data sources (databases, APIs)
- New analysis types
- Real-time data needs

### Visual Gaps
- New image types
- Interactive graphics
- Video editing

### Integration Gaps
- API connections
- Data import/export
- Workflow automation

### Analysis Gaps
- New metrics
- ML/AI capabilities
- Complex calculations

### Quality Gaps
- Review processes
- Validation checks
- Compliance needs

---

## Urgency Assessment

### Critical (Address This Week)
- Blocks primary workflows
- Multiple users affected
- No workaround exists

### High (Address This Month)
- Significant workflow friction
- Workaround is time-consuming
- Requested 3+ times

### Medium (Address This Quarter)
- Nice to have
- Workaround exists
- Requested 1-2 times

### Low (Backlog)
- Edge case
- Easy workaround
- Single request

---

## Gap Logging Triggers for Claude

When you (Claude) encounter these situations, log a gap:

### Automatic Triggers
1. You say "I can't" or "I don't have"
2. You suggest an external tool
3. User says "I wish" or "it would be nice"
4. Same topic comes up 3+ times in a week
5. User expresses frustration about capability

### Manual Triggers
1. End of complex session with unmet needs
2. New industry trend or tool emerges
3. User compares to competitor capability
4. Workflow requires multiple tools

---

## Gap Documentation Template

When logging a gap, include:

```
Request: [What was asked for]
Context: [The situation/workflow]
Category: [content-creation/research/visual/etc.]
Urgency: [critical/high/medium/low]
Potential Skill: [Suggested name]
Similar Existing: [Any related skills]
```

---

## Weekly Gap Review Process

1. **Monday Morning Review**
   - Run `python gap_analyzer.py --report`
   - Identify high-priority gaps

2. **Pattern Detection**
   - Look for keyword clusters
   - Check for frequency spikes

3. **Proposal Generation**
   - Create proposals for top 3 gaps
   - Review with skill templates

4. **Decision Making**
   - Approve/defer/reject proposals
   - Update backlog

5. **Communication**
   - Log decisions
   - Update gap statuses

---

*Reference for recognizing and documenting capability gaps.*
