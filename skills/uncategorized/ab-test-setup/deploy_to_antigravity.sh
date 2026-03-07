#!/bin/bash
# Deploy ab-test-setup skill to Antigravity skills directory

mkdir -p ~/.gemini/skills/ab-test-setup/
cp -r /a0/usr/projects/skillbuilder/solutions/ab-test-setup/* ~/.gemini/skills/ab-test-setup/
chmod +x ~/.gemini/skills/ab-test-setup/*.sh
chmod +x ~/.gemini/skills/ab-test-setup/scripts/*.py

echo "✅ A/B Test Setup skill deployed to ~/.gemini/skills/ab-test-setup/"
echo "Run test: bash ~/.gemini/skills/ab-test-setup/test.sh"
