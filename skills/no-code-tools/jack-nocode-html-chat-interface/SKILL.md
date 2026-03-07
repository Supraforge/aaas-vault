---
name: jack-nocode-html-chat-interface
description: >-
  Creates a simple HTML chat interface with file upload and settings modal,
  designed to connect to a webhook for AI interactions.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - html
  - chat interface
  - file upload
  - settings modal
  - webhook
  - ai
  - javascript
triggers:
  - When you need a simple chat interface for interacting with an AI backend.
  - When you need to send text messages and files to a webhook.
allowed-tools: []
compatibility: 'text editor, web browser'
metadata:
  source: jack-school
  lesson: 49
  lesson_title: How to Build an AI Productivity Agent (Save HOURS)
  difficulty: medium
  category: nocode
  tools_required:
    - text editor
    - web browser
  estimated_setup_time: 30min
---

# Nocode Html Chat Interface

## When to Use

Use this skill when you need to:
- When you need a simple chat interface for interacting with an AI backend.
- When you need to send text messages and files to a webhook.

## What This Does

Creates a simple HTML chat interface with file upload and settings modal, designed to connect to a webhook for AI interactions.

## Workflow

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Your AI Jarvis 🧠</title>
<style>
/* Chat App Styles */
.chat-app-container {
font-family: 'Avenir', Arial, sans-serif;
background-color: #eef5ff;
position: relative;
max-width: 600px;
margin: 10px auto;
border-radius: 10px;
box-shadow: 0 0 10px rgba(0,0,0,0.1);
overflow: hidden;
}


.chat-app-header {
background: linear-gradient(90deg, #00d2ff, #3a7bd5);
background-size: 200% 200%;
animation: chat-app-gradient-animation 5s ease infinite;
color: white;
padding: 15px;
font-size: 24px;
font-weight: bold;
display: flex;
justify-content: space-between;
align-items: center;
}


@keyframes chat-app-gradient-animation {
0% {
background-position: 0% 50%;
}
50% {
background-position: 100% 50%;
}
100% {
background-position: 0% 50%;
}
}


.chat-app-header-title {
flex: 1;
text-align: center;
}


.chat-app-message-display {
height: 400px;
padding: 10px;
overflow-y: auto;
background-color: #eef5ff;
}


.chat-app-message {
margin: 10px;
padding: 10px;
max-width: 70%;
word-wrap: break-word;
border-radius: 10px;
display: block;
position: relative;
opacity: 0;
animation: chat-app-fade-in 0.5s forwards;
}


@keyframes chat-app-fade-in {
to {
opacity: 1;
}
}


.chat-app-user-message {
background-color: #dcf8c6;
align-self: flex-end;
text-align: left;
margin-left: auto;
}


.chat-app-bot-message {
background-color: white;
align-self: flex-start;
text-align: left;
margin-right: auto;
}


.chat-app-input-container {
display: flex;
align-items: center;
padding: 10px;
background-color: #f0f0f0;
}


.chat-app-message-input {
flex: 1;
padding: 10px;
font-size: 16px;
border: none;
border-radius: 20px;
background-color: white;
margin: 0 10px;
height: 40px;
line-height: 20px;
resize: none;
overflow: auto;
}


.chat-app-message-input:focus {
outline: none;
}


.chat-app-send-button {
background-color: #128c7e;
color: white;
border: none;
padding: 10px;
font-size: 20px;
cursor: pointer;
border-radius: 50%;
width: 40px;
height: 40px;
display: flex;
align-items: center;
justify-content: center;
}


.chat-app-send-button:hover {
background-color: #075e54;
}


.chat-app-attach-button {
background-color: transparent;
color: #128c7e;
border: none;
padding: 0 10px;
font-size: 24px;
cursor: pointer;
}


.chat-app-attach-button:hover {
color: #075e54;
}


.chat-app-file-input {
display: none;
}


/* Modal Styles */
.chat-app-modal-overlay {
display: none;
position: fixed;
top: 0;
left: 0;
width: 100%;
height: 100%;
background: rgba(0,0,0,0.5);
z-index: 1000;
}


.chat-app-settings-modal {
display: none;
position: fixed;
top: 50%;
left: 50%;
width: 300px;
transform: translate(-50%, -50%);
background-color: white;
padding: 20px;
border-radius: 10px;
z-index: 1001;
display: flex;
flex-direction: column;
}


.chat-app-settings-modal h2 {
margin-top: 0;
}


.chat-app-settings-modal label {
display: block;
margin: 10px 0 5px;
}


.chat-app-settings-modal input[type="text"] {
width: 100%;
padding: 5px;
font-size: 16px;
margin-bottom: 15px;
}


.chat-app-settings-modal button {
padding: 10px;
width: 100%;
font-size: 16px;
cursor: pointer;
background-color: #128c7e;
color: white;
border: none;
border-radius: 5px;
}


.chat-app-settings-modal button:hover {
background-color: #075e54;
}


/* Style for images in chat */
.chat-app-message img {
max-width: 100%;
border-radius: 10px;
}


/* Style for PDF links */
.chat-app-pdf-link {
color: #1a0dab;
text-decoration: underline;
}


/* Remove border from settings cog and show on focus */
#chat-app-settings-button {
background-color: transparent;
border: none;
padding: 0 10px;
cursor: pointer;
}


#chat-app-settings-button:focus,
#chat-app-settings-button:active {
outline: none;
border: 1px solid #128c7e;
border-radius: 4px;
}


/* Remove default button focus outline */
button:focus {
outline: none;
}


</style>
<!-- Include Font Awesome for icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
<!-- Include Nunito font as a free alternative to Avenir -->
<link href="https://fonts.googleapis.com/css2?family=Nunito&display=swap" rel="stylesheet">
</head>
<body>


<!-- Chat App Container -->
<div class="chat-app-container">
<div class="chat-app-header">
<div class="chat-app-header-title">Your AI Jarvis 🧠</div>
<button class="chat-app-button" id="chat-app-settings-button">
<!-- Using Font Awesome icon for better visuals -->
<i class="fas fa-cog" style="font-size: 24px; color: white;"></i>
</button>
</div>
<div class="chat-app-message-display" id="chat-app-message-display"></div>
<div class="chat-app-input-container">
<input type="file" id="chat-app-file-input" class="chat-app-file-input" multiple>
<button class="chat-app-attach-button" id="chat-app-attach-button">
<i class="fas fa-paperclip"></i>
</button>
<textarea id="chat-app-message-input" class="chat-app-message-input" placeholder="Type a message"></textarea>
<button class="chat-app-send-button" id="chat-app-send-button">
<i class="fas fa-paper-plane"></i>
</button>
</div>
</div>


<!-- Modal Overlay -->
<div class="chat-app-modal-overlay" id="chat-app-modal-overlay"></div>


<!-- Settings Modal -->
<div class="chat-app-settings-modal" id="chat-app-settings-modal">
<h2>Settings</h2>
<label for="chat-app-passkey-input">Enter Pass Key:</label>
<input type="text" id="chat-app-passkey-input" placeholder="Pass Key">
<button id="chat-app-save-settings">Save Settings</button>
</div>


<script>
(function() {
const webhookUrl = 'https://hook.eu2.make.com/doprp2wzbtchmqqsfeyh7h6ola53jq1b';
let passKey = '';


// Get elements
const chatAppContainer = document.querySelector('.chat-app-container');
const messageDisplay = document.getElementById('chat-app-message-display');
const messageInput = document.getElementById('chat-app-message-input');
const sendButton = document.getElementById('chat-app-send-button');
const fileInput = document.getElementById('chat-app-file-input');
const attachButton = document.getElementById('chat-app-attach-button');
const settingsButton = document.getElementById('chat-app-settings-button');


const modalOverlay = document.getElementById('chat-app-modal-overlay');
const settingsModal = document.getElementById('chat-app-settings-modal');
const passkeyInput = document.getElementById('chat-app-passkey-input');
const saveSettingsButton = document.getElementById('chat-app-save-settings');


// Event listeners
sendButton.addEventListener('click', sendMessage);
messageInput.addEventListener('keyup', function(event) {
if (event.key === 'Enter' && !event.shiftKey) {
event.preventDefault();
sendMessage();
}
});
attachButton.addEventListener('click', () => fileInput.click());
fileInput.addEventListener('change', sendFiles);
settingsButton.addEventListener('click', openSettings);
modalOverlay.addEventListener('click', closeSettings);
saveSettingsButton.addEventListener('click', saveSettings);


function sendMessage() {
const messageText = messageInput.value.trim();
if (messageText === '') return;


displayMessage(messageText, 'chat-app-user-message');
messageInput.value = '';


// Send message to webhook with pass key
fetch(webhookUrl, {
method: 'POST',
headers: {
'Content-Type': 'application/json',
},
body: JSON.stringify({ text: messageText, passKey: passKey }),
})
.then(response => response.text())
.then(data => {
displayMessage(data, 'chat-app-bot-message');
})
.catch(error => {
console.error('Error:', error);
});
}


function sendFiles() {
const files = fileInput.files;
if (files.length === 0) return;


const formData = new FormData();
formData.append('passKey', passKey);
for (const file of files) {
formData.append('files', file);


if (file.type.startsWith('image/')) {
const reader = new FileReader();
reader.onload = function(e) {
displayImage(e.target.result, 'chat-app-user-message');
}
reader.readAsDataURL(file);
} else if (file.type === 'application/pdf') {
displayPDFLink(file.name, URL.createObjectURL(file), 'chat-app-user-message');
} else {
displayMessage(`Sent a file: ${file.name}`, 'chat-app-user-message');
}
}


// Send files to webhook
fetch(webhookUrl, {
method: 'POST',
body: formData,
})
.then(response => response.text())
.then(data => {
displayMessage(data, 'chat-app-bot-message');
})
.catch(error => {
console.error('Error:', error);
});


// Reset file input
fileInput.value = '';
}


function displayMessage(message, className) {
const messageElement = document.createElement('div');
messageElement.classList.add('chat-app-message', className);
messageElement.innerHTML = formatMessage(message);
messageDisplay.appendChild(messageElement);
messageDisplay.scrollTop = messageDisplay.scrollHeight;
}


function displayImage(src, className) {
const messageElement = document.createElement('div');
messageElement.classList.add('chat-app-message', className);
const img = document.createElement('img');
img.src = src;
messageElement.appendChild(img);
messageDisplay.appendChild(messageElement);
messageDisplay.scrollTop = messageDisplay.scrollHeight;
}


function displayPDFLink(filename, url, className) {
const messageElement = document.createElement('div');
messageElement.classList.add('chat-app-message', className);
const link = document.createElement('a');
link.href = url;
link.target = '_blank';
link.textContent = filename;
link.classList.add('chat-app-pdf-link');
messageElement.appendChild(link);
messageDisplay.appendChild(messageElement);
messageDisplay.scrollTop = messageDisplay.scrollHeight;
}


function formatMessage(text) {
return text.replace(/\n/g, '<br>').replace(/ /g, '&nbsp;&nbsp;');
}


function openSettings() {
settingsModal.style.display = 'flex';
modalOverlay.style.display = 'block';
// Remove focus from the settings button to hide the border
settingsButton.blur();
}


function closeSettings() {
settingsModal.style.display = 'none';
modalOverlay.style.display = 'none';
}


function saveSettings() {
// Save pass key
passKey = passkeyInput.value;


closeSettings();
}
})();
</script>
</body>
</html>

## Configuration

**Required tools/platforms:**
- text editor
- web browser

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
