// TikTok Analytics Script
const TikTokClient = require('./server').TikTokClient;
const fs = require('fs');
const path = require('path');

async function generateAnalyticsReport(videoIds) {
  const client = new TikTokClient();
  const reports = [];
  
  for (const videoId of videoIds) {
    try {
      const analytics = await client.getVideoAnalytics(videoId);
      reports.push({
        videoId,
        analytics,
        timestamp: new Date().toISOString()
      });
    } catch (error) {
      console.error(`Failed to get analytics for video ${videoId}:`, error.message);
    }
  }
  
  // Save to CSV
  const csvContent = reports.map(r => 
    `${r.videoId},${r.analytics.engagement?.like_count || 0},${r.analytics.engagement?.comment_count || 0},${r.timestamp}`
  ).join('\n');
  
  const csvHeader = 'video_id,likes,comments,timestamp\n';
  const csvData = csvHeader + csvContent;
  
  fs.writeFileSync('tiktok_analytics.csv', csvData);
  console.log('Analytics report saved to tiktok_analytics.csv');
  
  return reports;
}

module.exports = { generateAnalyticsReport };
