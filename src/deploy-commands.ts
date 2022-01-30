const { SlashCommandBuilder } = require('@discordjs/builders');
const { REST } = require('@discordjs/rest');
const { Routes } = require('discord-api-types/v9');

const guildId = process.env.GUILDID;
const clientId = process.env.CLIENTID;
const token = process.env.TOKEN;

const commands = [
  new SlashCommandBuilder().setName('ping').setDescription('Replies with pong'),
]

  .map((command) => command.toJSON());

const rest = new REST({ version: '9' }).setToken(token);

rest.put(Routes.applicationGuildCommands(clientId, guildId, { body: commands }))
  .then(() => console.log('Sucessfully registered application commands.'))
  .catch(console.error);
