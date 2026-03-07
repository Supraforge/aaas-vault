#!/bin/bash
# Deploy 3d-web-experience skill to Antigravity skills directory

mkdir -p ~/.gemini/skills/3d-web-experience/
cp -r /a0/usr/projects/skillbuilder/solutions/3d-web-experience/* ~/.gemini/skills/3d-web-experience/
chmod +x ~/.gemini/skills/3d-web-experience/*.sh
chmod +x ~/.gemini/skills/3d-web-experience/scripts/*.py

echo "✅ 3D Web Experience skill deployed to ~/.gemini/skills/3d-web-experience/"
echo "Run test: bash ~/.gemini/skills/3d-web-experience/test.sh"
