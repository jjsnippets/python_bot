# import necessary libraries
from discord.ext import commands
import discord
import os
from dotenv import load_dotenv

# supplementary libraries
from datetime import datetime

# API token set-up
load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_DEBUG = int(os.getenv('CHANNEL_ID'))

# bot object creation
# intents = discord.Intents.default()
# intents.message_content = True
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@client.event
async def on_ready():
    # prints how many servers the bot is in
    guild_count = 0
    for guild in client.guilds:
        print(f" = {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1
    print("basic_bot is in " + str(guild_count) + " guilds.\n\n")

    # sends a message to the debug channel
    channel = client.get_channel(CHANNEL_DEBUG)
    await channel.send("I'm online: " + datetime.now().strftime("%b %d, %Y %I:%M:%S %p"))

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@client.event
async def on_message(message):
    # echoes '!hello' message from user
    if message.content == "!hello":
        await message.channel.send("hello echo")

client.run(BOT_TOKEN)