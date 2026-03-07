---
name: jack-design-react-dashboard
description: >-
  Generates a React-based interactive dashboard with a dark theme, integrating
  with Airtable using a user-provided base ID and featuring various components.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - react
  - dashboard
  - airtable
  - dark theme
  - recharts
  - chatbot
  - typescript
triggers:
  - When you need to generate a React dashboard
  - When you want to visualize data from Airtable in a dark-themed interface
allowed-tools: []
compatibility: 'claude, react, airtable'
metadata:
  source: jack-school
  lesson: 60
  lesson_title: Steal this $100k Bolt.New Dashboard... (INSANE)
  difficulty: hard
  category: design
  tools_required:
    - claude
    - react
    - airtable
  estimated_setup_time: 1hr
  extracted_from:
    - $100 AI Dashboard Prompt.txt
---

# Design React Dashboard

## When to Use

Use this skill when you need to:
- When you need to generate a React dashboard
- When you want to visualize data from Airtable in a dark-themed interface

## What This Does

Generates a React-based interactive dashboard with a dark theme, integrating with Airtable using a user-provided base ID and featuring various components.

## Workflow

Create a modular, responsive React-based interactive dashboard that integrates with Airtable using a user-provided base ID (pass key). The dashboard should feature a dark theme with the specified color scheme and include the following components and functionalities:

Authentication:
Add a pass key input on the homepage allowing users to enter their Airtable base ID.
Validate the base ID and securely fetch data using the provided Airtable API token.
Sidebar 

Navigation:
Implement a responsive sidebar with navigation tabs for "Dashboard," "Overview," "Chat," "Team," "Tasks," "Reports," and "Settings."
Highlight the selected tab and display notifications where applicable.

Main Content Area:
Automations & Efficiency Section:
Display interactive line charts for Automations, Efficiency, and Conversations.
Ensure month labels are visible and properly formatted.
Include total counts and trend indicators.

Financial Overview Tabs:
Create tabs for "Income" and "Expenses."
Show total Income YTD, total Expenses YTD, Operating Profit YTD, and Profit Margin percentage.

Add separate graphs for Income and Expenses with accurate calculations and proper scaling.
Include future projections that can be toggled via a button, displaying projected data in a distinct color.

Additional Metrics:
Display Total Conversations from the Airtable data.
Ensure all numerical values are correctly formatted (e.g., in thousands) and calculations are accurate.

Data Visualization:
Use Recharts for interactive and responsive charts.
Implement tooltips, legends, and hover effects for better user experience.
Add future projection elements with dashed lines and clear indicators.

Chatbot Integration:
Add an "Ask Me Anything" chatbot with an input box that sends user queries to the webhook https://hook.eu2.make.com/g5u9qg2bc3dsi937rlsethkc84zdm184.
Display responses from the webhook within the chat interface.
Ensure the chat window is accessible via the "Chat" tab and is visible when activated.

Error Handling & Validation:
Implement robust error handling for Airtable data fetching (e.g., unauthorized access, data not found).
Validate user inputs for the pass key and handle loading states gracefully.

Deployment:
Prepare the application for deployment on platforms like Netlify.
Ensure secure handling of Airtable API tokens using environment variables.
Optimize the build for performance and responsiveness across all devices.

Styling:
Apply the provided CSS styles for a consistent dark theme.
Ensure all components adhere to the design specifications, including fonts, colors, and spacing.

Remove any unnecessary gradient borders and enhance overall visual appeal.

Technical Requirements:
Use React with TypeScript for type safety.
Modularize components for maintainability (e.g., Sidebar, MenuItem, Content, Chatbot, Tabs).
Utilize React Hooks (useState, useEffect) for state management.
Implement animations using React Spring where appropriate.
Ensure accessibility and responsiveness across different screen sizes.


Use the below code to create this:
@import url('https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200;0,300;0,400;0,600;0,700;0,800;0,900;1,200;1,300;1,400;1,600;1,700;1,800;1,900&display=swap');
body{
font-family: 'Nunito', sans-serif;
color:#676767;
background-color: #1e1e1e;
}
.bg-card{
background-color:#171717;
}
.bg-sidebar-card-top{
background-color: #353535;
}
.sidebar-separator-top{
border-bottom: 1px solid #2e2e2e;
}
.sidebar-separator-bottom{
border-top: 1px solid #2e2e2e;
}
.text-premium-yellow{
color: #f7b91c;
}
.icon-background{
background: #2d2d2d;
}
.tooltip-head{
background: #1d1d1d;
}
.tooltip-body{
background:#252525 ;
}
.search-icon{
top: 50%;
transform: translate(0, -50%);
}
.card-stack-border{
border-bottom: 2px solid #696969;
}
.bg-details{
background-color: #1e1e1e;
}
.add-component-head{
background-color: #181818;
background-image: url("https://www.transparenttextures.com/patterns/carbon-fibre.png");
}
.sidebar-item-selected{
color: white;
border-right: 2px solid white;
}
.sidebar-item{
border-right: 2px solid transparent;
}
.sidebar-item:hover {
color:#a1a0a0;
}

## Configuration

**Required tools/platforms:**
- claude
- react
- airtable

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
