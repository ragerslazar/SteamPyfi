import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from Model.SteamGames import SteamGames

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

@client.tree.command(name="price", description="Récupérer les infos sur un jeu Steam")
async def price_command(interaction: discord.Interaction, game_id: int):
    game = SteamGames(game_id)
    game_info = game.getInfo()


    if game_info is False:
        await interaction.response.send_message("Ce jeu n'éxiste pas.")
    elif float(game_info[0]) > 0:
        embed = discord.Embed(
            title=f"🎮 {game_info[1]}",
            description= "Informations sur " + game_info[1] + " ⬇️",
            color=discord.Color.random()
        )
        embed.set_thumbnail(url="https://i.ibb.co/bMHxWb66/steam.jpg")
        embed.add_field(name="💰 Prix", value=f"{game_info[0]} €", inline=False)
        embed.add_field(name="🔥 Réduction", value=f"{game_info[2]}", inline=True)
        embed.add_field(name="🏷️ Prix après réduction", value=f"{game_info[3]}", inline=True)
        #embed.set_footer(text="Footer text")

        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(
            title=f"🎮 {game_info[1]}",
            description= "Informations sur " + game_info[1] + " ⬇️",
            color=discord.Color.random()
        )
        embed.add_field(name="🏷️ Test", value="cc", inline=True)
        #embed.set_footer(text="Footer text")

        await interaction.response.send_message(embed=embed)
client.run(TOKEN)