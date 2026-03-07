# The Systematic Debugging Process

### Phase 1: Reproduce
1. **Reproducibility Check**: Can you trigger it randomly or always?
2. **Minimal Reproduction**: Create a smallest example that fails. Isolate from unrelated code.
3. **Document Steps**: Capture exact steps and environment state.

### Phase 2: Gather Information
- **Error Messages**: Full stack traces and log output.
- **Environment**: OS version, Runtime version, Dependency versions.
- **Recent Changes**: Git history and deployment timeline.
- **Scope**: Who is affected? Which browsers/environments?

### Phase 3: Form Hypothesis
- **What changed?** Recent code, dependency, or infra updates.
- **What's different?** Working vs broken environment/user.
- **Where could this fail?** Input validation, logic, data layer, or services.

### Phase 4: Test & Verify
- **Binary Search**: Comment out halves to narrow the scope.
- **Strategic Logging**: Track variables and execution flow.
- **Isolate Components**: Test pieces separately with mocks.
- **Compare**: Diff configurations and data.
