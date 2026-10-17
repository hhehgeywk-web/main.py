import os
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'مرحبا':
        await message.channel.send('هلا والله! منور السيرفر ✨')

client.run(os.getenv('TOKEN'))
