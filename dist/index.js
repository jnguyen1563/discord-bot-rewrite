"use strict";
const { Client, Intents } = require('discord.js');
const { token } = require('../config.json');
const client = new Client({ intents: [Intents.FLAGS.GUIDS] });
client.once('ready', () => {
    console.log('Bot is logged in');
});
client.login(token);
//# sourceMappingURL=index.js.map