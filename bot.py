import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="ticket", description="Create a ticket panel")
@app_commands.describe(option="Choose an option", button_text="Text for the button", image_url="URL of the image")
async def ticket(interaction: discord.Interaction, option: str, button_text: str, image_url: str):
    embed = discord.Embed(title="Ticket Panel", description="Choose an option below:", color=discord.Color.blue())
    if image_url:
        embed.set_image(url=image_url)

    view = discord.ui.View()
    button = discord.ui.Button(label=button_text, style=discord.ButtonStyle.primary)
    view.add_item(button)

    await interaction.response.send_message(embed=embed, view=view)

bot.run(TOKEN)