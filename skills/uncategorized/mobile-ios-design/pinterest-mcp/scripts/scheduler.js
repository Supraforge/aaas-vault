#!/usr/bin/env node

const PinterestAPI = require('./pinterest_api.js');
const fs = require('fs');
const path = require('path');

class PinterestScheduler {
    constructor() {
        this.api = new PinterestAPI();
        this.scheduleFile = 'pinterest_schedule.json';
    }
    
    async loadSchedule() {
        try {
            if (fs.existsSync(this.scheduleFile)) {
                const data = fs.readFileSync(this.scheduleFile, 'utf8');
                return JSON.parse(data);
            }
            return [];
        } catch (error) {
            console.error('Error loading schedule:', error.message);
            return [];
        }
    }
    
    async saveSchedule(schedule) {
        try {
            fs.writeFileSync(this.scheduleFile, JSON.stringify(schedule, null, 2));
            console.log(`✅ Schedule saved to ${this.scheduleFile}`);
        } catch (error) {
            console.error('Error saving schedule:', error.message);
        }
    }
    
    async addToSchedule(boardId, imageUrl, description, scheduleTime) {
        try {
            const schedule = await this.loadSchedule();
            
            const newItem = {
                id: Date.now().toString(),
                board_id: boardId,
                image_url: imageUrl,
                description: description,
                schedule_time: scheduleTime,
                status: 'scheduled',
                created_at: new Date().toISOString()
            };
            
            schedule.push(newItem);
            await this.saveSchedule(schedule);
            
            console.log(`✅ Added to schedule: ${description}`);
            console.log(`   Scheduled for: ${scheduleTime}`);
            
            return newItem;
        } catch (error) {
            console.error('❌ Failed to add to schedule:', error.message);
            throw error;
        }
    }
    
    async processScheduledPins() {
        try {
            const schedule = await this.loadSchedule();
            const now = new Date();
            
            const dueItems = schedule.filter(item => 
                item.status === 'scheduled' && 
                new Date(item.schedule_time) <= now
            );
            
            if (dueItems.length === 0) {
                console.log('No scheduled pins due for posting');
                return [];
            }
            
            console.log(`📅 Processing ${dueItems.length} scheduled pins...`);
            
            const results = [];
            
            for (const item of dueItems) {
                try {
                    console.log(`  Posting: ${item.description.substring(0, 50)}...`);
                    
                    const result = await this.api.createPin(
                        item.board_id,
                        item.image_url,
                        item.description
                    );
                    
                    // Update status
                    item.status = 'posted';
                    item.posted_at = new Date().toISOString();
                    item.pin_id = result.id;
                    
                    results.push({
                        item,
                        result,
                        success: true
                    });
                    
                    console.log(`    ✅ Posted successfully (ID: ${result.id})`);
                    
                } catch (error) {
                    console.error(`    ❌ Failed to post: ${error.message}`);
                    item.status = 'failed';
                    item.error = error.message;
                    
                    results.push({
                        item,
                        error: error.message,
                        success: false
                    });
                }
                
                // Small delay between posts
                await new Promise(resolve => setTimeout(resolve, 1000));
            }
            
            // Save updated schedule
            await this.saveSchedule(schedule);
            
            console.log(`✅ Processed ${results.filter(r => r.success).length} pins successfully`);
            console.log(`   Failed: ${results.filter(r => !r.success).length}`);
            
            return results;
            
        } catch (error) {
            console.error('❌ Failed to process scheduled pins:', error.message);
            throw error;
        }
    }
}

// Command line interface
if (require.main === module) {
    const scheduler = new PinterestScheduler();
    
    const command = process.argv[2];
    
    switch (command) {
        case 'add':
            if (process.argv.length < 7) {
                console.log('Usage: node scheduler.js add <boardId> <imageUrl> <description> <scheduleTime>');
                console.log('Example: node scheduler.js add 123456 https://example.com/image.jpg "Product launch" "2024-01-22T10:00:00Z"');
                process.exit(1);
            }
            scheduler.addToSchedule(process.argv[3], process.argv[4], process.argv[5], process.argv[6]);
            break;
            
        case 'process':
            scheduler.processScheduledPins();
            break;
            
        case 'list':
            scheduler.loadSchedule().then(schedule => {
                console.log('📅 Scheduled pins:');
                schedule.forEach(item => {
                    console.log(`  ${item.schedule_time}: ${item.description.substring(0, 50)} (${item.status})`);
                });
            });
            break;
            
        default:
            console.log('Available commands:');
            console.log('  add <boardId> <imageUrl> <description> <scheduleTime>');
            console.log('  process - Process due scheduled pins');
            console.log('  list - List all scheduled pins');
    }
}

module.exports = PinterestScheduler;
