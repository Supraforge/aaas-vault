---
name: jack-content-html-whatsapp-chat-interface
description: >-
  Generates HTML code for a web app with a WhatsApp-style chat interface for
  displaying AI-generated responses.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - HTML
  - CSS
  - JavaScript
  - web app
  - chat interface
  - AI panel
  - confetti animation
  - timer
triggers:
  - When building a web application with a chat interface
  - When visualizing responses from an AI expert panel
allowed-tools: []
compatibility: 'HTML editor, web browser'
metadata:
  source: jack-school
  lesson: 36
  lesson_title: This AI Meeting Automation 100Xs Your Productivity
  difficulty: medium
  category: content
  tools_required:
    - HTML editor
    - web browser
  estimated_setup_time: 30min
  extracted_from:
    - WhatsApp_Chat_HTML_.txt
---

# Content Html Whatsapp Chat Interface

## When to Use

Use this skill when you need to:
- When building a web application with a chat interface
- When visualizing responses from an AI expert panel

## What This Does

Generates HTML code for a web app with a WhatsApp-style chat interface for displaying AI-generated responses.

## Workflow

<div id="panel-discussion-container">
<style>
#panel-discussion-container {
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
display: flex;
justify-content: center;
align-items: center;
padding: 20px;
background-color: #ffffff;
}
#panel-discussion-container .container {
width: 100%;
max-width: 1200px;
background-color: #fff;
border-radius: 10px;
border: 1px solid #000;
box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
#panel-discussion-container .chat-header {
background-color: #075e54;
color: white;
padding: 10px;
border-top-left-radius: 10px;
border-top-right-radius: 10px;
}
#panel-discussion-container .chat-body {
height: 500px;
overflow-y: auto;
padding: 20px;
position: relative;
}
#panel-discussion-container .input-area {
display: flex;
padding: 10px;
background-color: #f0f0f0;
border-bottom-left-radius: 10px;
border-bottom-right-radius: 10px;
}
#panel-discussion-container #questionInput {
flex-grow: 1;
padding: 10px;
border: 1px solid #ccc;
border-radius: 20px;
margin-right: 10px;
min-height: 100px;
resize: vertical;
}
#panel-discussion-container button {
background-color: #075e54;
color: white;
border: none;
padding: 10px 20px;
border-radius: 20px;
cursor: pointer;
align-self: flex-end;
}
#panel-discussion-container iframe {
width: 100%;
height: 100%;
border: none;
}
#panel-discussion-container .loading {
position: absolute;
top: 0;
left: 0;
right: 0;
bottom: 0;
background-color: rgba(255, 255, 255, 0.9);
display: flex;
justify-content: center;
align-items: center;
z-index: 1000;
flex-direction: column;
}
#panel-discussion-container .loading-spinner {
width: 50px;
height: 50px;
border: 5px solid #f3f3f3;
border-top: 5px solid #3498db;
border-radius: 50%;
animation: spin 1s linear infinite;
}
#panel-discussion-container .countdown {
margin-top: 10px;
font-size: 18px;
font-weight: bold;
}
#panel-discussion-container .loading-message {
margin-top: 20px;
font-size: 18px;
text-align: center;
max-width: 80%;
}
@keyframes spin {
0% { transform: rotate(0deg); }
100% { transform: rotate(360deg); }
}
#panel-discussion-container .confetti {
position: absolute;
width: 10px;
height: 10px;
background-color: #f0f0f0;
position: absolute;
top: -10px;
z-index: 1001;
animation: confetti 5s ease-in-out -2s infinite;
transform-origin: left top;
}
#panel-discussion-container .confetti:nth-child(1) { background-color: #3498db; left: 10%; }
#panel-discussion-container .confetti:nth-child(2) { background-color: #2ecc71; left: 20%; }
#panel-discussion-container .confetti:nth-child(3) { background-color: #e74c3c; left: 30%; }
#panel-discussion-container .confetti:nth-child(4) { background-color: #f39c12; left: 40%; }
#panel-discussion-container .confetti:nth-child(5) { background-color: #9b59b6; left: 50%; }
#panel-discussion-container .confetti:nth-child(6) { background-color: #1abc9c; left: 60%; }
#panel-discussion-container .confetti:nth-child(7) { background-color: #e67e22; left: 70%; }
#panel-discussion-container .confetti:nth-child(8) { background-color: #34495e; left: 80%; }
@keyframes confetti {
0% { transform: rotateZ(15deg) rotateY(0deg) translate(0,0); }
25% { transform: rotateZ(5deg) rotateY(360deg) translate(-5vw,20vh); }
50% { transform: rotateZ(15deg) rotateY(720deg) translate(5vw,60vh); }
75% { transform: rotateZ(5deg) rotateY(1080deg) translate(-10vw,80vh); }
100% { transform: rotateZ(15deg) rotateY(1440deg) translate(10vw,110vh); }
}
</style>
<div class="container">
<div class="chat-header">
<h2>Expert Panel Discussion</h2>
</div>
<div class="chat-body">
<iframe name="chatFrame" src="about:blank"></iframe>
<div class="loading" style="display: none;">
<div class="loading-spinner"></div>
<div class="countdown">80</div>
<div class="loading-message">Congratulations! The AI panel has begun. Please wait a moment while we prepare your responses.</div>
</div>
<div class="confetti" style="display: none;"></div>
<div class="confetti" style="display: none;"></div>
<div class="confetti" style="display: none;"></div>
<div class="confetti" style="display: none;"></div>
<div class="confetti" style="display: none;"></div>
<div class="confetti" style="display: none;"></div>
<div class="confetti" style="display: none;"></div>
<div class="confetti" style="display: none;"></div>
</div>
<div class="input-area">
<form id="questionForm" action="https://hook.eu2.make.com/7byvtdb9q6gw4nvi7q4sq2nijyx2bqif" method="POST">
<textarea id="questionInput" name="question" placeholder="Ask your question..." required></textarea>
<button type="submit">Send</button>
</form>
</div>
</div>


<script>
document.getElementById('questionForm').addEventListener('submit', function(e) {
e.preventDefault();
var question = document.getElementById('questionInput').value;
var formData = new FormData();
formData.append('question', question);


var xhr = new XMLHttpRequest();
xhr.open('POST', this.action, true);
xhr.onload = function() {
if (xhr.status === 200) {
document.querySelector('iframe[name="chatFrame"]').srcdoc = xhr.responseText;
}
};
xhr.send(formData);
startLoading();
});


function startLoading() {
var loadingElement = document.querySelector('#panel-discussion-container .loading');
var countdownElement = document.querySelector('#panel-discussion-container .countdown');
var confettiElements = document.querySelectorAll('#panel-discussion-container .confetti');
var questionInput = document.querySelector('#panel-discussion-container #questionInput');
var submitButton = document.querySelector('#panel-discussion-container button');


loadingElement.style.display = 'flex';
confettiElements.forEach(el => el.style.display = 'block');
questionInput.disabled = true;
submitButton.disabled = true;


var countdown = 80;
var countdownInterval = setInterval(function() {
countdown--;
countdownElement.textContent = countdown;
if (countdown <= 0) {
clearInterval(countdownInterval);
loadingElement.style.display = 'none';
confettiElements.forEach(el => el.style.display = 'none');
questionInput.disabled = false;
submitButton.disabled = false;
}
}, 1000);
}
</script>
</div>

## Configuration

**Required tools/platforms:**
- HTML editor
- web browser

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
