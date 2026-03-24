#\!/bin/bash
echo "Testing skill: research-protocol"
python3 "$(dirname "$0")/../scripts/"*.py --help 2>/dev/null || echo "No runnable scripts found"
echo "SKILL.md exists: $(test -f "$(dirname "$0")/../SKILL.md" && echo YES || echo NO)"
