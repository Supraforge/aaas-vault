---
id: follow_up
name: Meeting Follow-Up Email
category: email
tags: [follow-up, meeting, sales]
description: Post-meeting follow-up email with summary and next steps
variables:
  - name: prospect_name
    required: true
    description: Prospect's first name
  - name: meeting_topic
    required: true
    description: What the meeting was about
  - name: key_points
    required: true
    description: 2-3 key discussion points
  - name: next_steps
    required: true
    description: Agreed next steps
  - name: timeline
    required: false
    default: next week
  - name: sender_name
    required: false
    default: Tobias
---

# Meeting Follow-Up Email

**Subject:** Following up: {{ meeting_topic }}

Hi {{ prospect_name }},

Thank you for taking the time to discuss {{ meeting_topic }} today.

## Key Points We Covered

{{ key_points }}

## Agreed Next Steps

{{ next_steps }}

## Timeline

I'll follow up {{ timeline }} to check on progress. In the meantime, don't hesitate to reach out if any questions come up.

Looking forward to continuing the conversation.

Best,
{{ sender_name }}

---

## Usage Notes

- Send within 2 hours of meeting
- Keep key points to 3-5 bullets max
- Next steps should be specific and actionable
- Include any promised materials as attachments
