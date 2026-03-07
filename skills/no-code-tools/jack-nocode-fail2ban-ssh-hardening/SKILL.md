---
name: jack-nocode-fail2ban-ssh-hardening
description: >-
  Provides commands to enhance SSH security by installing fail2ban and changing
  the SSH port.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - ssh
  - security
  - fail2ban
  - hardening
  - vps
triggers:
  - securing SSH
  - hardening VPS security
allowed-tools: []
compatibility: 'terminal, ssh'
metadata:
  source: jack-school
  lesson: 130
  lesson_title: ClawdBot gives you Superpowers... lets Unlock them
  difficulty: medium
  category: nocode
  tools_required:
    - terminal
    - ssh
  estimated_setup_time: 30min
---

# Nocode Fail2ban Ssh Hardening

## When to Use

Use this skill when you need to:
- securing SSH
- hardening VPS security

## What This Does

Provides commands to enhance SSH security by installing fail2ban and changing the SSH port.

## Workflow

# On your VPS, run as root:
# Install fail2ban
apt-get update && apt-get install -y fail2ban
systemctl enable fail2ban && systemctl start fail2ban
# Change SSH port to 2222
ufw allow 2222/tcp
echo "Port 2222" >> /etc/ssh/sshd_config
# Disable socket activation and restart SSH
systemctl stop ssh.socket 2>/dev/null || true
systemctl disable ssh.socket 2>/dev/null || true
systemctl enable sshd && systemctl restart sshd
# Test new port in a NEW terminal (keep current session open):
ssh -p 2222 root@YOUR_VPS_IP
# Once confirmed working, remove old port:
sed -i '/^Port 22$/d' /etc/ssh/sshd_config
systemctl restart sshd
ufw delete allow 22/tcp
apt-get upgrade -y

# Update local SSH config (~/.ssh/config on your Mac):
Host myvps
    HostName YOUR_VPS_IP
    Port 2222
    User root
    IdentityFile ~/.ssh/YOUR_KEY_NAME

# Now connect with: ssh myvps

## Configuration

**Required tools/platforms:**
- terminal
- ssh

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
