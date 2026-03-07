---
name: jack-email-customer-review-request
description: >-
  Sends a personalized email asking for a customer review, with rating options
  linked to a webhook.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - email
  - customer feedback
  - review request
  - html
triggers:
  - after a customer interaction
  - when seeking customer feedback
allowed-tools: []
compatibility: 'email client, make.com (optional)'
metadata:
  source: jack-school
  lesson: 35
  lesson_title: Steal this $97/mo Google Review Automation
  difficulty: medium
  category: email
  tools_required:
    - email client
    - make.com (optional)
  estimated_setup_time: 30min
  extracted_from:
    - ⭐️ Review Email ⭐️.txt
---

# Email Customer Review Request

## When to Use

Use this skill when you need to:
- after a customer interaction
- when seeking customer feedback

## What This Does

Sends a personalized email asking for a customer review, with rating options linked to a webhook.

## Workflow

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rate Our Service</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
    <h1 style="color: #2c3e50;">How did we do?</h1>
    <p>Howdy {{1.`Name 👋`}},</p>
    <p>Thank you for choosing us, we'd love your feedback. How was your experience today?</p>
    
    <div style="display: flex; flex-wrap: wrap; justify-content: space-between; margin-top: 20px;">
        <a href="https://hook.eu2.make.com/0g25vjdcoevgwaudidf4wkusmj7sbanb6?rating=1&email={{1.`Email 📧`}}" style="background-color: #FF4136; color: white; border: none; padding: 10px 15px; margin: 5px; font-size: 14px; text-decoration: none; border-radius: 5px; text-align: center; display: inline-block;">1 - Poor</a>
        <a href="https://hook.eu2.make.com/0g25vjdcoevgwaudidf4wkusmj7sbanb6?rating=2&email={{1.`Email 📧`}}" style="background-color: #FF851B; color: white; border: none; padding: 10px 15px; margin: 5px; font-size: 14px; text-decoration: none; border-radius: 5px; text-align: center; display: inline-block;">2 - Fair</a>
        <a href="https://hook.eu2.make.com/0g25vjdcoevgwaduidf4wkusmj7sbanb6?rating=3&email={{1.`Email 📧`}}" style="background-color: #FFDC00; color: black; border: none; padding: 10px 15px; margin: 5px; font-size: 14px; text-decoration: none; border-radius: 5px; text-align: center; display: inline-block;">3 - Good</a>
        <a href="https://hook.eu2.make.com/0g25vjdcoevgdwauidf4wkusmj7sbanb6?rating=4&email={{1.`Email 📧`}}" style="background-color: #2ECC40; color: white; border: none; padding: 10px 15px; margin: 5px; font-size: 14px; text-decoration: none; border-radius: 5px; text-align: center; display: inline-block;">4 - Great </a>
        <a href="https://hook.eu2.make.com/0g25vjdcoevgdwauidf4wkusmj7sbanb6?rating=5&email={{1.`Email 📧`}}" style="background-color: #0074D9; color: white; border: none; padding: 10px 15px; margin: 5px; font-size: 14px; text-decoration: none; border-radius: 5px; text-align: center; display: inline-block;">5 - Excellent</a>
    </div>
    
    <p>Your feedback helps us to be better.</p>
    <p>I appreciate you,</p>
    <p>{{1.`Barber 💈`}}</p>


    <table cellpadding="0" cellspacing="0" border="0" style="vertical-align: -webkit-baseline-middle; font-size: medium; font-family: Arial;">
        <tbody>
            <tr>
                <td>
                    <table cellpadding="0" cellspacing="0" border="0" style="vertical-align: -webkit-baseline-middle; font-size: medium; font-family: Arial;">
                        <tbody>
                            <tr>
                                <td style="vertical-align: top;">
                                    <table cellpadding="0" cellspacing="0" border="0" style="vertical-align: -webkit-baseline-middle; font-size: medium; font-family: Arial;">
                                        <tbody>
                                            <tr>
                                                <td style="text-align: center;">
                                                    <img src="https://imgs.search.brave.com/p-3L5AbXp7Zf7Vowj8wv-UdSlKO3C-Nzb0ztDX6oeT4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzAyLzEwLzk3LzE5/LzM2MF9GXzIxMDk3/MTk1OV93WGNCWWZp/ZjdqS2V5S2tIS2hW/eU9uelFXSGF3SWdL/NC5qcGc" role="presentation" width="130" style="display: block; max-width: 128px;">
                                                </td>
                                            </tr>
                                            <tr>
                                                <td height="30"></td>
                                            </tr>
                                            <tr>
                                                <td style="text-align: center;">
                                                    <table cellpadding="0" cellspacing="0" border="0" style="display: inline-block; vertical-align: -webkit-baseline-middle; font-size: medium; font-family: Arial;">
                                                        <tbody>
                                                            <tr style="text-align: center;">
                                                                <td>
                                                                    <a href="//qerger" style="display: inline-block; padding: 0px; background-color: rgb(112, 117, 219);">
                                                                        <img src="https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/facebook-icon-2x.png" alt="facebook" width="24" style="background-color: rgb(112, 117, 219); max-width: 135px; display: block;">
                                                                    </a>
                                                                </td>
                                                                <td width="5">
                                                                    <div></div>
                                                                </td>
                                                                <td>
                                                                    <a href="//erg" style="display: inline-block; padding: 0px; background-color: rgb(112, 117, 219);">
                                                                        <img src="https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/twitter-icon-2x.png" alt="twitter" width="24" style="background-color: rgb(112, 117, 219); max-width: 135px; display: block;">
                                                                    </a>
                                                                </td>
                                                                <td width="5">
                                                                    <div></div>
                                                                </td>
                                                                <td>
                                                                    <a href="//asdfref" style="display: inline-block; padding: 0px; background-color: rgb(112, 117, 219);">
                                                                        <img src="https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/linkedin-icon-2x.png" alt="linkedin" width="24" style="background-color: rgb(112, 117, 219); max-width: 135px; display: block;">
                                                                    </a>
                                                                </td>
                                                                <td width="5">
                                                                    <div></div>
                                                                </td>
                                                                <td>
                                                                    <a href="//eqrger" style="display: inline-block; padding: 0px; background-color: rgb(112, 117, 219);">
                                                                        <img src="https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/instagram-icon-2x.png" alt="instagram" width="24" style="background-color: rgb(112, 117, 219); max-width: 135px; display: block;">
                                                                    </a>
                                                                </td>
                                                                <td width="5">
                                                                    <div></div>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                                <td width="46">
                                    <div></div>
                                </td>
                                <td style="padding: 0px; vertical-align: middle;">
                                    <h2 style="margin: 0px; font-size: 18px; color: rgb(0, 0, 0); font-weight: 600;">
                                        <span>Barber Barberr</span>
                                        <span>&nbsp;</span>
                                        <span></span>
                                    </h2>
                                    <table cellpadding="0" cellspacing="0" border="0" style="width: 100%; vertical-align: -webkit-baseline-middle; font-size: medium; font-family: Arial;">
                                        <tbody>
                                            <tr>
                                                <td height="30"></td>
                                            </tr>
                                            <tr>
                                                <td style="width: 100%; border-bottom: 1px solid rgb(164, 12, 63); border-left: none; display: block;"></td>
                                            </tr>
                                            <tr>
                                                <td height="30"></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <table cellpadding="0" cellspacing="0" border="0" style="vertical-align: -webkit-baseline-middle; font-size: medium; font-family: Arial;">
                                        <tbody>
                                            <tr height="25" style="vertical-align: middle;">
                                                <td width="30" style="vertical-align: middle;">
                                                    <table cellpadding="0" cellspacing="0" border="0" style="vertical-align: -webkit-baseline-middle; font-size: medium; font-family: Arial;">
                                                        <tbody>
                                                            <tr>
                                                                <td style="vertical-align: bottom;">
                                                                    <span style="display: inline-block; background-color: rgb(164, 12, 63);">
                                                                        <img src="https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/phone-icon-2x.png" alt="mobilePhone" width="13" style="display: block; background-color: rgb(164, 12, 63);">
                                                                    </span>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                                <td style="padding: 0px; color: rgb(0, 0, 0);">
                                                    <a href="tel:0777 777 7777 " style="text-decoration: none; color: rgb(0, 0, 0); font-size: 12px;">
                                                        <span>0777 777 7777 </span>
                                                    </a>
                                                </td>
                                            </tr>
                                            <tr height="25" style="vertical-align: middle;">
                                                <td width="30" style="vertical-align: middle;">
                                                    <table cellpadding="0" cellspacing="0" border="0" style="vertical-align: -webkit-baseline-middle; font-size: medium; font-family: Arial;">
                                                        <tbody>
                                                            <tr>
                                                                <td style="vertical-align: bottom;">
                                                                    <span style="display: inline-block; background-color: rgb(164, 12, 63);">
                                                                        <img src="https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/link-icon-2x.png" alt="website" width="13" style="display: block; background-color: rgb(164, 12, 63);">
                                                                    </span>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                                <td style="padding: 0px;">
                                                    <a href="//barberbarberrr.co" style="text-decoration: none; color: rgb(0, 0, 0); font-size: 12px;">
                                                        <span>barberbarberrr.co</span>
                                                    </a>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <table cellpadding="0" cellspacing="0" border="0" style="vertical-align: -webkit-baseline-middle; font-size: medium; font-family: Arial;">
                                        <tbody>
                                            <tr>
                                                <td height="30"></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
            </tr>
        </tbody>
    </table>
</body>
</html>

## Configuration

**Required tools/platforms:**
- email client
- make.com (optional)

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
