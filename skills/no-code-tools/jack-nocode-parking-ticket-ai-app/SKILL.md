---
name: jack-nocode-parking-ticket-ai-app
description: >-
  HTML template for a parking ticket portal with audio recording, photo upload,
  and data submission functionality.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - html
  - javascript
  - audio recording
  - photo upload
  - form submission
  - parking ticket app
triggers:
  - building a web app with audio recording
  - building a web app with photo upload
  - creating a data submission form
allowed-tools: []
compatibility: 'browser, microphone, camera'
metadata:
  source: jack-school
  lesson: 46
  lesson_title: Steal this micro AI SaaS (100% Automated)
  difficulty: medium
  category: nocode
  tools_required:
    - browser
    - microphone
    - camera
  estimated_setup_time: 30min
---

# Nocode Parking Ticket Ai App

## When to Use

Use this skill when you need to:
- building a web app with audio recording
- building a web app with photo upload
- creating a data submission form

## What This Does

HTML template for a parking ticket portal with audio recording, photo upload, and data submission functionality.

## Workflow

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Parking Ticket Portal</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>
body, html {
font-family: 'Inter', sans-serif;
margin: 0;
padding: 0;
height: 100%;
background-color: #f0f2f5;
display: flex;
justify-content: center;
align-items: center;
}
.card {
background-color: white;
border-radius: 20px;
box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
width: 90%;
max-width: 400px;
overflow: hidden;
position: relative;
}
.card::before {
content: '';
position: absolute;
top: 0;
left: 0;
right: 0;
height: 5px;
background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%);
}
.card-content {
padding: 20px;
}
h1 {
font-size: 24px;
color: #333;
margin: 0 0 20px;
text-align: center;
}
.action-buttons {
display: flex;
justify-content: space-between;
margin-bottom: 20px;
}
.button {
flex: 1;
padding: 12px;
border: none;
border-radius: 8px;
font-size: 14px;
font-weight: 600;
cursor: pointer;
transition: all 0.3s ease;
}
#recordButton {
background-color: #FF4757;
color: white;
}
#uploadButton {
background-color: #5352ED;
color: white;
margin: 0 10px;
}
#takePhotoButton {
background-color: #2ED573;
color: white;
}
.button:hover {
opacity: 0.9;
transform: translateY(-2px);
}
#sendButton {
display: block;
width: 100%;
padding: 14px;
background-color: #3742FA;
color: white;
border: none;
border-radius: 8px;
font-size: 16px;
font-weight: 600;
cursor: pointer;
transition: all 0.3s ease;
margin-top: 20px;
}
#sendButton:hover {
background-color: #2C36F2;
}
.preview-container {
margin-top: 20px;
text-align: center;
}
#photoPreview {
max-width: 100%;
border-radius: 8px;
display: none;
}
#audioPreview {
width: 100%;
margin-top: 10px;
display: none;
}
.status-bar {
background-color: #F1F2F6;
padding: 15px;
text-align: center;
font-size: 14px;
color: #57606F;
border-top: 1px solid #E3E7F1;
}
.status-item {
display: inline-flex;
align-items: center;
margin: 0 10px;
}
.status-icon {
margin-right: 5px;
font-size: 18px;
}
.recording-animation {
height: 40px;
display: flex;
align-items: center;
justify-content: center;
margin-bottom: 20px;
}
.waveform {
display: flex;
align-items: center;
height: 100%;
}
.wave-bar {
width: 3px;
background-color: #FF4757;
margin: 0 1px;
height: 100%;
}
.recording-dot {
width: 10px;
height: 10px;
background-color: #FF4757;
border-radius: 50%;
margin-left: 10px;
}
</style>
</head>
<body>
<div class="card">
<div class="card-content">
<h1>Parking Ticket Portal</h1>
<div class="recording-animation" id="recordingAnimation" style="display: none;">
<div class="waveform">
<div class="wave-bar"></div>
<div class="wave-bar"></div>
<div class="wave-bar"></div>
<div class="wave-bar"></div>
<div class="wave-bar"></div>
<div class="wave-bar"></div>
<div class="wave-bar"></div>
<div class="wave-bar"></div>
<div class="wave-bar"></div>
<div class="wave-bar"></div>
</div>
<div class="recording-dot"></div>
</div>
<div class="action-buttons">
<button id="recordButton" class="button">🎤 Record</button>
<button id="uploadButton" class="button">📷 Upload</button>
<button id="takePhotoButton" class="button">📸 Take Photo</button>
</div>
<div class="preview-container">
<img id="photoPreview" alt="Photo preview">
<audio id="audioPreview" controls></audio>
</div>
<button id="sendButton">Send Data</button>
</div>
<div class="status-bar">
<span class="status-item" id="audioStatus">
<span class="status-icon">❌</span>
<span class="status-text">Audio: Not recorded</span>
</span>
<span class="status-item" id="photoStatus">
<span class="status-icon">❌</span>
<span class="status-text">Photo: Not uploaded</span>
</span>
</div>
</div>

<input type="file" id="photoInput" accept="image/*" style="display: none;">

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
<script>
const recordButton = document.getElementById('recordButton');
const uploadButton = document.getElementById('uploadButton');
const takePhotoButton = document.getElementById('takePhotoButton');
const sendButton = document.getElementById('sendButton');
const photoInput = document.getElementById('photoInput');
const photoPreview = document.getElementById('photoPreview');
const audioPreview = document.getElementById('audioPreview');
const audioStatus = document.getElementById('audioStatus');
const photoStatus = document.getElementById('photoStatus');
const recordingAnimation = document.getElementById('recordingAnimation');
const waveBars = document.querySelectorAll('.wave-bar');

let isRecording = false;
let audioBlob = null;
let photo = null;
let mediaRecorder = null;
let audioContext = null;
let analyser = null;
let dataArray = null;

recordButton.addEventListener('click', toggleRecording);
uploadButton.addEventListener('click', () => photoInput.click());
photoInput.addEventListener('change', handlePhotoUpload);
takePhotoButton.addEventListener('click', takePhoto);
sendButton.addEventListener('click', sendData);

async function toggleRecording() {
if (!isRecording) {
try {
const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
startRecording(stream);
} catch (err) {
console.error("Error accessing microphone:", err);
alert("Error accessing microphone. Please ensure you have granted microphone permissions.");
}
} else {
stopRecording();
}
}

function startRecording(stream) {
isRecording = true;
mediaRecorder = new MediaRecorder(stream);
audioContext = new AudioContext();
analyser = audioContext.createAnalyser();
const source = audioContext.createMediaStreamSource(stream);
source.connect(analyser);
analyser.fftSize = 256;
dataArray = new Uint8Array(analyser.frequencyBinCount);

let chunks = [];
mediaRecorder.ondataavailable = (e) => chunks.push(e.data);
mediaRecorder.onstop = () => {
audioBlob = new Blob(chunks, { type: 'audio/ogg; codecs=opus' });
audioPreview.src = URL.createObjectURL(audioBlob);
audioPreview.style.display = 'block';
};

mediaRecorder.start();
recordButton.style.backgroundColor = '#FF6B6B';
recordButton.textContent = '⏹ Stop';
recordingAnimation.style.display = 'flex';
updateAudioStatus(true);
animateWaveform();
}

function stopRecording() {
isRecording = false;
mediaRecorder.stop();
mediaRecorder.stream.getTracks().forEach(track => track.stop());
recordButton.style.backgroundColor = '#FF4757';
recordButton.textContent = '🎤 Record';
recordingAnimation.style.display = 'none';
updateAudioStatus(false);
cancelAnimationFrame(animationFrame);
}

let animationFrame;
function animateWaveform() {
analyser.getByteFrequencyData(dataArray);
for (let i = 0; i < waveBars.length; i++) {
const value = dataArray[i * 2];
const percent = value / 255;
const height = percent * 100;
waveBars[i].style.height = height + '%';
}
animationFrame = requestAnimationFrame(animateWaveform);
}

function updateAudioStatus(recording) {
const icon = audioStatus.querySelector('.status-icon');
const text = audioStatus.querySelector('.status-text');
if (recording) {
icon.textContent = '🔴';
text.textContent = 'Audio: Recording...';
} else if (audioBlob) {
icon.textContent = '✅';
text.textContent = 'Audio: Recorded';
} else {
icon.textContent = '❌';
text.textContent = 'Audio: Not recorded';
}
}

function handlePhotoUpload(event) {
const file = event.target.files[0];
if (file) {
const reader = new FileReader();
reader.onload = (e) => {
photoPreview.src = e.target.result;
photoPreview.style.display = 'block';
updatePhotoStatus(true);
};
reader.readAsDataURL(file);
photo = file;
}
}

function updatePhotoStatus(uploaded) {
const icon = photoStatus.querySelector('.status-icon');
const text = photoStatus.querySelector('.status-text');
if (uploaded) {
icon.textContent = '✅';
text.textContent = 'Photo: Uploaded';
} else {
icon.textContent = '❌';
text.textContent = 'Photo: Not uploaded';
}
}

function takePhoto() {
alert('Camera functionality would be implemented here.');
// Simulating a photo taken
updatePhotoStatus(true);
}

async function sendData() {
if (!audioBlob && !photo) {
alert('Please record audio or upload/take a photo before sending.');
return;
}

const formData = new FormData();
if (audioBlob) formData.append('audio', audioBlob, 'recording.ogg');
if (photo) formData.append('photo', photo);

try {
const response = await fetch('https://hook.eu2.make.com/vculst1yx93gfkhlnp6wzwmw3e6ayytgh', {
method: 'POST',
body: formData
});

if (response.ok) {
confetti({
particleCount: 100,
spread: 70,
origin: { y: 0.6 }
});
alert('Data sent successfully!');
// Reset the form after successful send
audioBlob = null;
photo = null;
photoPreview.style.display = 'none';
audioPreview.style.display = 'none';
updateAudioStatus(false);
updatePhotoStatus(false);
} else {
throw new Error('Failed to send data');
}
} catch (error) {
console.error('Error sending data:', error);
alert('Failed to send data. Please try again.');
}
}
</script>
</body>
</html>

## Configuration

**Required tools/platforms:**
- browser
- microphone
- camera

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
