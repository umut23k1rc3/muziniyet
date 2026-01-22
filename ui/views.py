import discord
from discord.ui import View, Button
from services.database import save_interest
from services.recommendation import recommend

class InterestView(View):
    def __init__(self, user_id):
        super().__init__(timeout=60)
        self.user_id = user_id

    @discord.ui.button(label="Technology", style=discord.ButtonStyle.primary)
    async def tech(self, interaction: discord.Interaction, button: Button):
        await self.process(interaction, "Technology")

    @discord.ui.button(label="Creative", style=discord.ButtonStyle.success)
    async def creative(self, interaction: discord.Interaction, button: Button):
        await self.process(interaction, "Creative")

    async def process(self, interaction, interest):
        save_interest(self.user_id, interest)
        careers = recommend(interest)

        msg = f"**Recommended Careers ({interest})**\n\n"
        for c in careers:
            msg += (
                f"**{c['name']}**\n"
                f"Salary: {c['salary_tr']}\n"
                f"{c['description']}\n\n"
            )

        await interaction.response.send_message(msg, ephemeral=True)


