import discord
from discord.ext import commands
from config import TOKEN
from services.database import init_db
from ui.views import InterestView

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    init_db()
    print(f"Bot logged in as {bot.user}")

@bot.command()
async def start(ctx):
    await ctx.send(
        "🎯 **Career Guidance Bot**\nSelect your interest:",
        view=InterestView(ctx.author.id)
    )

bot.run(TOKEN)

