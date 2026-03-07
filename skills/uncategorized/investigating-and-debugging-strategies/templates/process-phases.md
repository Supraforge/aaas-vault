# Systematic Debugging Process

### Phase 1: Reproduce
1. **Consistency**: Can you trigger it randomly or always?
2. **Minimalism**: Create a smallest example that fails. Isolate from unrelated code.
3. **Documentation**: Capture exact steps and environment state.

### Phase 2: Gather Information
- **Stack Traces**: Full context of the error.
- **Environment**: OS, Runtime, Dependency versions.
- **Recent Changes**: Git history and deployment logs.

### Phase 3: Form Hypothesis
- **What changed?** (Code, data, infra)
- **What's different?** (Dev vs Prod, working vs broken user)

### Phase 4: Test & Verify
- **Binary Search**: Comment out halves to narrow the scope.
- **Strategic Logging**: Track variables and flow.
- **Isolate Components**: Test each piece separately with mocks.
