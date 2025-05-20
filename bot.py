import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!" ,intents=intents)

@client.event
async def on_ready():
    try:
        sync = await client.tree.sync()
        print(f"Commandes slash synchro: {len(sync)}")
    except Exception as e:
        print(e)
    print(f'Logged on as {client.user}!')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    print(f'Message from {message.author}: {message.content}')

@client.tree.command(name="ping", description="Renvoie Pong !")
async def ping_command(interaction: discord.Interaction):
    await interaction.response.send_message("Pong")

client.run(TOKEN)