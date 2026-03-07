---
name: jack-design-dynamic-chart-dashboard
description: >-
  Generates a dynamic subscription dashboard with interactive charts using HTML,
  CSS, and JavaScript, fetching data from a Make.com webhook.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - dashboard
  - data visualization
  - chart.js
  - html
  - css
  - javascript
triggers:
  - when you need a visual representation of subscription data
  - when you want a dashboard that updates dynamically with webhook data
allowed-tools: []
compatibility: 'code editor, web browser'
metadata:
  source: jack-school
  lesson: 38
  lesson_title: Steal this AI-Powered Client Dashboard
  difficulty: medium
  category: design
  tools_required:
    - code editor
    - web browser
  estimated_setup_time: 30min
  extracted_from:
    - Graph_Visualisation_Code_.txt
---

# Design Dynamic Chart Dashboard

## When to Use

Use this skill when you need to:
- when you need a visual representation of subscription data
- when you want a dashboard that updates dynamically with webhook data

## What This Does

Generates a dynamic subscription dashboard with interactive charts using HTML, CSS, and JavaScript, fetching data from a Make.com webhook.

## Workflow

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Subscription Dashboard</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.0/chart.min.js"></script>
<style>
body {font-family: Arial, sans-serif;background-color: #1a1a1a;color: #ffffff;margin: 0;padding: 20px;}
.dashboard {background-color: #2a2a2a;border-radius: 10px;padding: 20px;box-shadow: 0 0 10px rgba(0,255,255,0.1);}
.header {display: flex;justify-content: flex-end;align-items: center;margin-bottom: 20px;}
.predict-btn {background-color: #00ff00;color: #000000;border: none;padding: 10px 20px;border-radius: 5px;cursor: pointer;transition: background-color 0.3s;}
.predict-btn:hover {background-color: #00cc00;}
#chart {width: 100%;height: 400px;}
</style>
</head>
<body>
<div class="dashboard">
<div class="header">
<button class="predict-btn" id="predictBtn">Predict Next Month</button>
</div>
<canvas id="chart"></canvas>
</div>
<script>
let chart;
function initChart(data) {
const ctx = document.getElementById('chart').getContext('2d');
chart = new Chart(ctx, {
type: 'line',
data: {
labels: data.labels,
datasets: [{
label: 'Total Subscribers',
data: data.subscribers,
borderColor: 'aqua',
tension: 0.1
}, {
label: 'New Sales',
data: data.sales,
borderColor: 'magenta',
tension: 0.1
}, {
label: 'Churn',
data: data.churn,
borderColor: 'cyan',
tension: 0.1
}]
},
options: {
responsive: true,
scales: {
y: {
beginAtZero: true,
grid: {
color: 'rgba(255, 255, 255, 0.1)'
},
ticks: {
color: 'white'
}
},
x: {
grid: {
color: 'rgba(255, 255, 255, 0.1)'
},
ticks: {
color: 'white'
}
}
},
plugins: {
legend: {
labels: {
color: 'white'
}
},
tooltip: {
mode: 'index',
intersect: false,
}
},
elements: {
point: {
radius: 0,
hoverRadius: 8,
}
}
}
});
}
function predictNextMonth(data) {
const lastThreeMonths = data.slice(-3);
const predictedValues = lastThreeMonths.reduce((acc, curr) => {
return {
subscribers: acc.subscribers + curr.subscribers,
sales: acc.sales + curr.sales,
churn: acc.churn + curr.churn
};
}, { subscribers: 0, sales: 0, churn: 0 });
return {
subscribers: Math.round(predictedValues.subscribers / 3),
sales: Math.round(predictedValues.sales / 3),
churn: Math.round(predictedValues.churn / 3)
};
}
const predictBtn = document.getElementById('predictBtn');
predictBtn.addEventListener('click', () => {
const prediction = predictNextMonth(chart.data.datasets[0].data.map((subscribers, i) => ({
subscribers,
sales: chart.data.datasets[1].data[i],
churn: chart.data.datasets[2].data[i]
})));
const nextMonth = (chart.data.labels.length % 12) + 1;
const monthName = new Date(2024, nextMonth - 1).toLocaleString('default', { month: 'short' });
chart.data.labels.push(monthName);
chart.data.datasets[0].data.push(prediction.subscribers);
chart.data.datasets[1].data.push(prediction.sales);
chart.data.datasets[2].data.push(prediction.churn);
chart.update();
});
const defaultData = {
labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
subscribers: [300, 284, 262, 240, 194, 287, 338, 292],
sales: [47, 85, 97, 3, 30, 12, 32, 8],
churn: [82, 31, 13, 92, 19, 97, 81, 52]
};
fetch('https://hook.eu2.make.com/4mlebpsy2pwigcehx7b3qabdxgkmxns1')
.then(response => response.text())
.then(text => {
const data = parseData(text);
if (data.labels.length === 0) {
console.warn('No data received from webhook. Using default data.');
initChart(defaultData);
} else {
initChart(data);
}
})
.catch(error => {
console.error('Error fetching data:', error);
console.warn('Using default data due to fetch error.');
initChart(defaultData);
});
function parseData(text) {
const lines = text.split('\n');
const data = {
labels: [],
subscribers: [],
sales: [],
churn: []
};
const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
lines.forEach(line => {
const parts = line.split(' ');
if (parts.length >= 8 && !isNaN(parseInt(parts[1]))) {
const monthIndex = parseInt(parts[1]) - 1;
data.labels.push(months[monthIndex]);
data.sales.push(parseInt(parts[3]));
data.churn.push(parseInt(parts[5]));
data.subscribers.push(parseInt(parts[7]));
}
});
return data;
}
</script>
</body>
</html>

## Configuration

**Required tools/platforms:**
- code editor
- web browser

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
