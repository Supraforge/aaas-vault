#!/bin/bash
# Install dependencies for this skill
pip install -r requirements.txt 2>/dev/null || echo "No requirements.txt found"
