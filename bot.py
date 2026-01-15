import discord
from discord.ext import commands

from config import TOKEN
from services.career_service import CareerService
from services.user_service import UserService
from ui.views import FieldSelectView

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

career_service = CareerService()
user_service = UserService()

@bot.event
async def on_ready():
    print("Career Guidance Bot is ONLINE")

@bot.command()
async def start(ctx):
    await ctx.send(
        "Welcome! Please choose your area of interest:",
        view=FieldSelectView(field_selected)
    )

async def field_selected(interaction: discord.Interaction):
    field = interaction.data["custom_id"]
    user_service.set_interest(interaction.user.id, field)

    title = career_service.get_title(field)
    careers = career_service.get_careers(field)

    message = "\n".join(f"- {career}" for career in careers)

    await interaction.response.send_message(
        f"**{title}**\n\nRecommended careers:\n{message}",
        ephemeral=True
    )

bot.run(TOKEN)
