const { Client, GatewayIntentBits } = require('discord.js');
require('dotenv').config();

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
        GatewayIntentBits.GuildMembers
    ]
});

client.on('ready', () => {
    console.log(`✅ Logged in as ${client.user.tag}!`);
    console.log(`📊 Serving ${client.guilds.cache.size} servers`);
    
    // Set bot status
    client.user.setActivity('Community Management', { type: 'WATCHING' });
});

client.on('messageCreate', async (message) => {
    // Ignore bot messages
    if (message.author.bot) return;
    
    // Basic command handling
    if (message.content === '!ping') {
        await message.reply('Pong!');
    }
    
    if (message.content === '!help') {
        await message.reply('Available commands: !ping, !help, !stats');
    }
});

client.on('guildMemberAdd', async (member) => {
    console.log(`👋 New member joined: ${member.user.tag}`);
    
    // Send welcome message
    const welcomeChannel = member.guild.systemChannel;
    if (welcomeChannel) {
        await welcomeChannel.send(`Welcome ${member} to ${member.guild.name}!`);
    }
});

// Login
const token = process.env.DISCORD_BOT_TOKEN;
if (!token) {
    console.error('❌ DISCORD_BOT_TOKEN not found in .env');
    process.exit(1);
}

client.login(token).catch(console.error);

// Handle graceful shutdown
process.on('SIGINT', () => {
    console.log('\n🛑 Shutting down Discord bot...');
    client.destroy();
    process.exit(0);
});
