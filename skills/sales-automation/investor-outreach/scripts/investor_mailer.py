#!/usr/bin/env python3
import os
import json
import argparse
import markdown
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from pathlib import Path

# Manual .env loading in case of permission issues
def load_env():
    # Try current dir .env, then local .env.local, then project root .env
    env_paths = [
        Path.cwd() / ".env",
        Path(__file__).parent / ".env.local",
        Path(__file__).parent.parent.parent.parent / ".env",
        Path("/tmp/sh_env")
    ]

    for env_path in env_paths:
        try:
            # We just try to open it directly; existence check might fail due to permissions
            with open(env_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if '=' in line and not line.startswith('#'):
                        key, value = line.split('=', 1)
                        os.environ[key] = value.strip("'").strip('"')
            return True
        except Exception:
            continue
    return False


load_env()

def send_investor_email(to_email, template_id, name_placeholder, attachment_path=None, blurb="", cc=None):
    """
    Sends an investor outreach email using Gmail SMTP.
    """
    gmail_user = os.getenv('INVESTOR_GMAIL_USER')
    gmail_password = os.getenv('INVESTOR_GMAIL_PASSWORD')
    
    if not gmail_user or not gmail_password:
        print("❌ Error: INVESTOR_GMAIL_USER or INVESTOR_GMAIL_PASSWORD not set in .env")
        return False

    # Load templates
    templates_path = Path(__file__).parent.parent / "resources" / "templates.json"
    try:
        with open(templates_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Error loading templates from {templates_path}: {e}")
        return False
    
    template = next((t for t in data['options'] if t['id'] == template_id), None)
    if not template:
        print(f"❌ Error: Template ID '{template_id}' not found.")
        return False

    subject = template['subject']
    
    # Process blurb (ensure it ends with a double newline if it exists)
    formatted_blurb = f"{blurb}\n\n" if blurb and len(blurb.strip()) > 0 else ""
    
    body_markdown = template['body']
    body_markdown = body_markdown.replace("[Name]", name_placeholder)
    body_markdown = body_markdown.replace("[Investor Name]", name_placeholder)
    body_markdown = body_markdown.replace("[Blurb]", formatted_blurb)

    msg = MIMEMultipart('alternative')
    msg['From'] = gmail_user
    msg['To'] = to_email
    msg['Subject'] = subject
    
    if cc:
        msg['Cc'] = cc

    # Convert Markdown to HTML
    body_html = markdown.markdown(body_markdown)
    
    styled_html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; }}
            a {{ color: #D4AF37; text-decoration: none; font-weight: bold; }}
        </style>
    </head>
    <body>
        {body_html}
    </body>
    </html>
    """
    
    msg.attach(MIMEText(body_markdown, 'plain'))
    msg.attach(MIMEText(styled_html, 'html'))

    if attachment_path and os.path.exists(attachment_path):
        try:
            with open(attachment_path, "rb") as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(attachment_path))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
            msg.attach(part)
        except Exception as e:
            print(f"❌ Error attaching file: {e}")
            return False

    try:
        print(f"📤 Preparing to send '{template['name']}' to {to_email}...")
        if cc:
            print(f"   📎 CC'ing: {cc}")
        
        # Check against sent log to prevent double-sends
        log_path = Path(__file__).parent.parent / "output" / "sent_log.json"
        if log_path.exists():
            try:
                with open(log_path, 'r') as f:
                    sent_data = json.load(f)
                if to_email in sent_data:
                    print(f"⚠️ Warning: Email already sent to {to_email} on {sent_data[to_email]}. Skipping.")
                    return True # Skip
            except Exception:
                pass
        
        # Use Port 587 (open in this env)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_password)
        
        # Combine recipients
        recipients = [to_email]
        if cc:
            recipients.append(cc)
            
        server.send_message(msg, from_addr=gmail_user, to_addrs=recipients)
        server.close()
        print(f"✅ Email sent successfully to {to_email}!")

        # Update sent log
        try:
            from datetime import datetime
            sent_data = {}
            if log_path.exists():
                with open(log_path, 'r') as f:
                    sent_data = json.load(f)
            
            sent_data[to_email] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_path.parent.mkdir(exist_ok=True)
            with open(log_path, 'w') as f:
                json.dump(sent_data, f, indent=2)
        except Exception as log_err:
            print(f"⚠️ Warning: Could not update sent_log: {log_err}")

        return True


    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send Investor Outreach Email")
    parser.add_argument("--to", required=True, help="Recipient email address")
    parser.add_argument("--template", required=True, choices=["traction-first", "tech-forward", "problem-solution"], help="Template ID to use")
    parser.add_argument("--name", required=True, help="Investor name for placeholder replacement")
    parser.add_argument("--blurb", default="", help="Personalized intro blurb")
    parser.add_argument("--attach", help="Path to attachment (e.g. pitch deck PDF)")

    args = parser.parse_args()
    send_investor_email(args.to, args.template, args.name, args.attach, args.blurb)

