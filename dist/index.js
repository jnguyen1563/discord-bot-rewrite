"use strict";
const { Client, Intents } = require('discord.js');
const dotenv = require('dotenv');
dotenv.config();
const client = new Client({
    intents: [Intents.FLAGS.GUIDS, Intents.FLAGS.GUILD_MESSAGES],
});
client.on('ready', () => {
    console.log('Bot is ready');
});
client.on('messageCreate', (message) => {
    if (message.content === 'ping') {
        message.reply({
            content: 'pong',
        });
    }
});
client.login(process.env.token);
//# sourceMappingURL=index.js.map