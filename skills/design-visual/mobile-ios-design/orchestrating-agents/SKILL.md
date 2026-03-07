---
name: orchestrating-agents
description: Orchestrates multiple agents through performance optimization, multi-agent coordination, and context management
version: 1.0.0
dependencies: ["python3", "jq", "git"]
---

# Agent Orchestration

## 🎯 Triggers
- "Optimize agent performance"
- "Coordinate multiple agents for complex tasks"
- "Manage agent context and memory"
- "Analyze agent performance metrics"
- "Improve agent prompts and workflows"
- "Handle multi-agent communication and handoffs"

## ⚡ Quick Start (Self-Check)
Before running complex orchestration, verify readiness:
- [ ] Run `bash ~/.gemini/skills/orchestrating-agents/test.sh` to check dependencies.
- [ ] Ensure you have access to agent performance data or logs.
- [ ] Verify you can create and manage multiple agent instances.

## 📋 Workflow

### Phase 1: Agent Performance Analysis
1. **Gather Performance Data**: Collect metrics from agent interactions over time
   - Task completion rates (successful vs failed)
   - Response accuracy and factual correctness
   - Tool usage efficiency and patterns
   - Average response time and token consumption
   - User satisfaction indicators and feedback patterns

2. **Analyze Failure Modes**: Categorize failures by root cause
   - Instruction misunderstanding
   - Knowledge gaps
   - Tool selection errors
   - Context management issues
   - Hallucination patterns

3. **Identify Optimization Opportunities**:
   - Prompt engineering improvements
   - Context enhancement strategies
   - Tool usage optimization
   - Workflow refinements

### Phase 2: Multi-Agent Coordination
1. **Task Decomposition**: Break complex tasks into independent sub-tasks
2. **Agent Assignment**: Match agent capabilities to task requirements
3. **Parallel Execution**: Dispatch agents concurrently for efficiency
4. **Result Aggregation**: Collect and synthesize outputs from all agents
5. **Conflict Resolution**: Handle inconsistencies between agent outputs

### Phase 3: Context Management
1. **Context Collection**: Gather relevant information for agent tasks
2. **Context Preparation**: Structure and format context for optimal use
3. **Context Distribution**: Share appropriate context with each agent
4. **Context Maintenance**: Update and refresh context as needed
5. **Context Archival**: Store historical context for future reference

### Phase 4: Continuous Improvement
1. **Performance Monitoring**: Track optimization impact over time
2. **A/B Testing**: Compare different prompt and workflow variations
3. **Rollback Capability**: Revert changes if performance degrades
4. **Documentation Updates**: Keep skill documentation current with improvements

## 🤖 System Instructions

### Agent Performance Optimization
- Use data-driven approach combining metrics, feedback, and prompt engineering
- Always establish baseline metrics before making changes
- Test improvements in controlled environments before full deployment
- Maintain rollback capabilities for production safety
- Document all changes and their impact on performance

### Multi-Agent Coordination
- Identify truly independent tasks for parallelization
- Ensure clear communication protocols between agents
- Handle agent failures gracefully with fallback strategies
- Balance workload distribution to avoid bottlenecks
- Verify agent outputs meet quality standards before aggregation

### Context Management
- Collect only relevant context to avoid information overload
- Structure context for easy consumption by agents
- Maintain context freshness and relevance
- Implement security and privacy controls for sensitive context
- Archive historical context for analysis and improvement

## 🛠️ Script Reference

### Performance Analysis Script
```bash
#!/bin/bash
# analyze-agent-performance.sh
# Collects and analyzes agent performance metrics

# Usage: ./analyze-agent-performance.sh --days 30 --output report.json

# This script would:
# 1. Gather performance data from logs
# 2. Calculate key metrics
# 3. Generate optimization recommendations
# 4. Output structured report
```

### Multi-Agent Dispatcher
```bash
#!/bin/bash
# dispatch-agents.sh
# Coordinates multiple agents for parallel task execution

# Usage: ./dispatch-agents.sh --tasks tasks.json --agents agents.json

# This script would:
# 1. Parse task requirements
# 2. Match tasks to appropriate agents
# 3. Dispatch agents in parallel
# 4. Monitor progress and collect results
# 5. Aggregate and validate outputs
```

### Context Manager
```bash
#!/bin/bash
# manage-context.sh
# Handles context collection, preparation, and distribution

# Usage: ./manage-context.sh --task "analyze project" --sources sources.json

# This script would:
# 1. Identify relevant context sources
# 2. Extract and structure context
# 3. Prepare context for agent consumption
# 4. Distribute context to appropriate agents
# 5. Archive context for future use
```

## 📊 Performance Metrics Dashboard

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Task Completion Rate | >95% | [Value] | ⚪ |
| Response Accuracy | >90% | [Value] | ⚪ |
| Average Response Time | <30s | [Value] | ⚪ |
| User Satisfaction | >4/5 | [Value] | ⚪ |
| Hallucination Rate | <2% | [Value] | ⚪ |

## 🔄 Continuous Improvement Cycle

1. **Measure** → Collect performance data
2. **Analyze** → Identify improvement opportunities
3. **Implement** → Make targeted optimizations
4. **Test** → Validate improvements
5. **Deploy** → Roll out successful changes
6. **Monitor** → Track ongoing performance

## ⚠️ Common Pitfalls to Avoid

- **Over-optimization**: Don't sacrifice reliability for marginal gains
- **Context overload**: Too much context can reduce agent effectiveness
- **Poor task decomposition**: Ensure tasks are truly independent
- **Inadequate monitoring**: Always track the impact of changes
- **Ignoring feedback**: User feedback is critical for improvement

## 🚀 Advanced Features

### Dynamic Agent Routing
- Route tasks to specialized agents based on complexity and requirements
- Load balance across available agent instances
- Failover to backup agents when primary agents fail

### Context-Aware Prompting
- Dynamically adjust prompts based on available context
- Optimize prompt length and structure for different task types
- Personalize prompts based on user preferences and history

### Performance Prediction
- Predict agent performance for new task types
- Estimate resource requirements and response times
- Identify potential failure modes before execution

## 📚 Further Reading

- Agent performance optimization best practices
- Multi-agent system design patterns
- Context management strategies for AI agents
- Prompt engineering techniques
- A/B testing methodologies for AI systems
