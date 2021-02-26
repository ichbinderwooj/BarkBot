import discord
import os

from replit import db
from dotenv import load_dotenv
from discord.ext import commands, tasks

from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(
    command_prefix="!",
    description="Bark bot is a general purpose bot.")

@bot.event
async def on_ready():
	print("Bot is ready!")

@commands.command(name="server", help="Gets support server link")
async def server(ctx):
  await ctx.send("https://discord.gg/Tayz2DWE2D")

keep_alive()

bot.run(TOKEN)