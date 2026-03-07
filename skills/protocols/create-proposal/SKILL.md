---
name: "create-pandadoc-proposal"
description: "Create a PandaDoc proposal, including client research, content generation, JSON creation, script execution, and follow-up email."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["proposal generation","pandadoc","sales enablement","client research","content creation"]
triggers:
  - "when the user wants to generate a PandaDoc proposal for a client."
  - "when a user needs to create a structured proposal from sales call notes or client data."
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "directive"
  original_file: "create_proposal.md"
---

# Create Pandadoc Proposal

## When to Use

When a user provides client information in structured bullet points for a proposal.,When a user provides a sales call transcript that needs to be converted into a proposal.,When needing to automatically generate a PandaDoc proposal from gathered client data and project details.

## What This Does

Create a PandaDoc proposal, including client research, content generation, JSON creation, script execution, and follow-up email.

## Workflow

Gather Client Information: Collect client details, project title, problems, benefits, duration, and value in structured format or extract from a call transcript.,Conduct Client Research (Optional): If website URL is available, fetch and analyze the client's website to understand their brand voice and recent context. Create a Client Research Summary.,Generate Content: Expand on the problems and benefits using the gathered information and Client Research Summary. Focus on revenue impact and ROI, and contextualize with client's brand voice.,Construct JSON: Create a JSON object including client info, project details, and generated content. Format with slide and contract footers with appropriate dates.,Execute Proposal Creation: Save the JSON to a file and run the `execution/create_proposal.py` script.,Send Follow-Up Email: Send a follow-up email to the client, thanking them and briefly outlining the proposed solution using a provided HTML template.,Notify User: Display the PandaDoc internal link to the user and confirm the successful sending of the follow-up email.

## Constraints

Ensure all required client and project information is gathered before generating content.,Use the `execution/create_proposal.py` script to create the proposal.,Adhere to specified tone and style guidelines for problem and benefit expansions.,The JSON must be valid and properly formatted before running the Python script.,The follow-up email must be sent in HTML format using the provided template and `gmail.send_email`.
