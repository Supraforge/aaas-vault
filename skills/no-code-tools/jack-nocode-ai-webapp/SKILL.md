---
name: jack-nocode-ai-webapp
description: >-
  Creates a basic AI-powered web app with a chat interface using HTML and
  JavaScript to interact with a Make.com webhook.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - web app
  - chat interface
  - javascript
  - html
  - api
triggers:
  - when you need a simple web based chat interface to call an api
allowed-tools: []
compatibility: none
metadata:
  source: jack-school
  lesson: 37
  lesson_title: How to Build an AI Web App... that Sells 24/7
  difficulty: medium
  category: nocode
  tools_required:
    - none
  estimated_setup_time: 30min
  extracted_from:
    - Bobby_Tanks_Code_.txt
---

# Nocode Ai Webapp

## When to Use

Use this skill when you need to:
- when you need a simple web based chat interface to call an api

## What This Does

Creates a basic AI-powered web app with a chat interface using HTML and JavaScript to interact with a Make.com webhook.

## Workflow

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Website with Chat</title>
<style>
body {
font-family: Arial, sans-serif;
background-color: #f0f0f0;
margin: 0;
}


.chat-container {
width: 400px;
height: 600px;
background-color: white;
border-radius: 10px;
box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
overflow: hidden;
display: flex;
flex-direction: column;
}


.chat-header {
background-color: #6a1b9a;
color: white;
padding: 20px;
text-align: center;
font-size: 1.5em;
}


.chat-body {
padding: 10px;
height: calc(100% - 120px); /* Adjust height according to header and footer */
overflow-y: auto;
flex: 1;
border-bottom: 1px solid #ddd;
display: flex;
flex-direction: column;
}


.chat-footer {
display: flex;
padding: 10px;
border-top: 1px solid #ddd;
}


.chat-footer input {
flex: 1;
padding: 10px;
border: 1px solid #ddd;
border-radius: 5px;
margin-right: 10px;
}


.chat-footer button {
background-color: #6a1b9a;
color: white;
border: none;
padding: 10px 15px;
border-radius: 5px;
cursor: pointer;
}


.chat-footer button:hover {
background-color: #4a0f70;
}


.message {
margin: 10px 0;
padding: 10px;
border-radius: 10px;
max-width: 70%;
word-wrap: break-word;
position: relative;
}


.message.user {
background-color: #dcf8c6;
align-self: flex-end;
margin-left: auto;
}


.message.genie {
background-color: #e5e5ea;
align-self: flex-start;
margin-right: auto;
}


.loading {
display: flex;
align-items: center;
justify-content: center;
}


.loading-animation {
border: 4px solid #f3f3f3;
border-top: 4px solid #6a1b9a;
border-radius: 50%;
width: 20px;
height: 20px;
animation: spin 1s linear infinite;
}


@keyframes spin {
0% { transform: rotate(0deg); }
100% { transform: rotate(360deg); }
}
</style>
</head>
<body>
<div id="chat-widget" class="chat-container">
<div class="chat-header">
<h2>Bobby Tanks</h2>
</div>
<div class="chat-body" id="chat-body">
<!-- Chat messages will appear here -->
</div>
<div class="chat-footer">
<input type="text" id="user-message" placeholder="Type a message...">
<button id="send-button">Send</button>
</div>
</div>


<script>
document.getElementById('send-button').addEventListener('click', sendMessage);
document.getElementById('user-message').addEventListener('keypress', function (e) {
if (e.key === 'Enter') {
sendMessage();
}
});


function sendMessage() {
const messageInput = document.getElementById('user-message');
const message = messageInput.value.trim();
if (message === '') return;


appendMessage('user', message);
messageInput.value = '';
displayLoading();


const messages = Array.from(document.querySelectorAll('.message'))
.map(msg => msg.textContent);


fetch('https://hook.eu2.make.com/fgj666cemjgu4ur5jl1kk35kvxh3e0de', {
method: 'POST',
headers: {
'Content-Type': 'application/json',
},
body: JSON.stringify({ messages }),
})
.then(response => {
console.log('Response status:', response.status);
if (!response.ok) {
throw new Error('Network response was not ok');
}
return response.text();
})
.then(text => {
console.log('Response text:', text);
removeLoading();
appendMessage('genie', text);
})
.catch(error => {
console.error('Error:', error);
removeLoading();
appendMessage('genie', 'Sorry, something went wrong. Please try again.');
});
}


function appendMessage(sender, message) {
const chatBody = document.getElementById('chat-body');
const messageElement = document.createElement('div');
messageElement.classList.add('message', sender);
messageElement.textContent = message;
chatBody.appendChild(messageElement);
chatBody.scrollTop = chatBody.scrollHeight;
}


function displayLoading() {
const chatBody = document.getElementById('chat-body');
const loadingElement = document.createElement('div');
loadingElement.classList.add('message', 'genie', 'loading');
const loadingAnimation = document.createElement('div');
loadingAnimation.classList.add('loading-animation');
loadingElement.appendChild(loadingAnimation);
loadingElement.id = 'loading';
chatBody.appendChild(loadingElement);
chatBody.scrollTop = chatBody.scrollHeight;
}


function removeLoading() {
const loadingElement = document.getElementById('loading');
if (loadingElement) {
loadingElement.remove();
}
}
</script>
</body>
</html>

## Configuration

**Required tools/platforms:**
- none

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
