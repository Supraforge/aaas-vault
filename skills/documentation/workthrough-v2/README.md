# Workthrough Documentation Skill

Automatically generate comprehensive documentation for all development work in a structured "workthrough" format.

## Purpose

This skill helps maintain a detailed record of all development activities by automatically creating structured documentation after completing coding tasks. Think of it as an automated development journal that captures context, changes, and verification results.

## What Gets Documented

- Feature implementations
- Bug fixes and error resolutions
- Code refactoring
- Configuration changes
- Dependency updates
- Build/compilation issue fixes
- Architecture changes

## Key Benefits

1. **Knowledge Retention**: Capture important decisions and context while fresh
2. **Team Communication**: Share detailed progress with team members
3. **Debugging Reference**: Quickly recall how similar issues were solved
4. **Onboarding**: Help new developers understand project evolution
5. **Project History**: Maintain a readable development timeline

## Usage

The skill activates automatically after development work is completed. Claude will:

1. Analyze all changes made during the session
2. Generate structured documentation following the workthrough template
3. Include code examples and verification results
4. Save to the `workthrough/` directory with a timestamped filename

## Example Output

See the test example in `workthrougt-test/test.md` which demonstrates:
- Clear title and overview
- Systematic documentation of changes
- Code examples with file paths
- Build verification results
- Professional formatting

## File Organization

Documents are saved as:
```
workthrough/YYYY-MM-DD-brief-description.md
```

Or organized by feature:
```
workthrough/feature-name/implementation.md
workthrough/bugfix/issue-123.md
```

## Integration

This skill works seamlessly with your existing workflow:
- No manual intervention required
- Activates automatically after development tasks
- Creates documentation in parallel with coding
- Captures both successes and failures (for learning)

## Quality Guidelines

Good workthrough docs should:
- ✅ Explain the "why" behind changes
- ✅ Include concrete code examples
- ✅ Show verification/test results
- ✅ Be readable by other developers
- ✅ Capture important decisions

Avoid:
- ❌ Overly verbose descriptions
- ❌ Missing context or reasoning
- ❌ Incomplete verification steps
- ❌ Vague explanations

## Tips

- Review generated docs occasionally to ensure quality
- Use workthrough docs during code reviews
- Reference past workthroughs when facing similar issues
- Archive old workthroughs periodically to keep repo clean
- Share particularly useful workthroughs with the team

## License

MIT - Feel free to customize and adapt for your needs.
