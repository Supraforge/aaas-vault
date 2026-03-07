# Language-Specific Debugging Tools

### JavaScript/TypeScript
- **debugger**: Pause execution.
- **Console Methods**: `console.table()`, `console.time()`, `console.trace()`.
- **Performance marks**: `performance.mark('start')`.
- **VS Code**: `launch.json` configuration for Node/Jest.

### Python
- **pdb / breakpoint()**: Built-in interactive debuggers.
- **ipdb**: Enhanced interaction.
- **Post-mortem**: `pdb.post_mortem()` after exceptions.
- **Profiling**: `cProfile` and `pstats`.

### Go
- **Delve (dlv)**: Strong CLI debugging.
- **runtime/debug**: `debug.PrintStack()`.
- **pprof**: CPU and memory profiling.
