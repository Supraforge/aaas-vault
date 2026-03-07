---
name: jack-nocode-security-script
description: >-
  Bash script to harden a VPS by updating packages, installing a firewall, and
  disabling password authentication for SSH.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - security
  - vps
  - hardening
  - bash
  - firewall
  - ssh
triggers:
  - securing VPS
  - automatic VPS security
allowed-tools: []
compatibility: terminal
metadata:
  source: jack-school
  lesson: 130
  lesson_title: ClawdBot gives you Superpowers... lets Unlock them
  difficulty: medium
  category: nocode
  tools_required:
    - terminal
  estimated_setup_time: 15min
---

# Nocode Security Script

## When to Use

Use this skill when you need to:
- securing VPS
- automatic VPS security

## What This Does

Bash script to harden a VPS by updating packages, installing a firewall, and disabling password authentication for SSH.

## Workflow

cat > security-hardening.sh << 'EOF'
#!/bin/bash
set -euo pipefail

PORT="${PORT:-18789}"

echo "==> Updating packages"
sudo apt-get update -y >/dev/null

echo "==> Installing firewall (ufw)"
sudo apt-get install -y ufw >/dev/null

echo "==> Enabling firewall safely (allow SSH first)"
sudo ufw allow OpenSSH >/dev/null
sudo ufw deny "${PORT}"/tcp >/dev/null
sudo ufw --force enable >/dev/null

echo "==> Firewall status:"
sudo ufw status

echo "==> Hardening SSH (disable password auth, keys only)"
sudo sed -i "s/#PasswordAuthentication yes/PasswordAuthentication no/" /etc/ssh/sshd_config
sudo sed -i "s/PasswordAuthentication yes/PasswordAuthentication no/" /etc/ssh/sshd_config
sudo systemctl restart sshd

echo
echo "✅ SETUP COMPLETE"
echo
echo "==> Next: Check ClawdBot help with: clawdbot --help"
EOF

chmod +x security-hardening.sh
./security-hardening.sh

## Configuration

**Required tools/platforms:**
- terminal

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
