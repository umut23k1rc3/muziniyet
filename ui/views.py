import discord
from discord.ui import View, Button
from services.database import save_interest
from services.recommendation import recommend

FIELDS = {
    "Technology": "💻",
    "Creative": "🎨",
    "Business": "📊",
    "Health": "🩺"
}

class CareerFieldView(View):
    def __init__(self, user_id):
        super().__init__(timeout=60)
        self.user_id = user_id

        for field, emoji in FIELDS.items():
            self.add_item(
                Button(
                    label=field,
                    emoji=emoji,
                    style=discord.ButtonStyle.primary,
                    custom_id=field
                )
            )

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user.id == self.user_id

    async def on_timeout(self):
        for item in self.children:
            item.disabled = True

class FieldButton(Button):
    def __init__(self, field, user_id):
        super().__init__(
            label=field,
            style=discord.ButtonStyle.primary
        )
        self.field = field
        self.user_id = user_id

    async def callback(self, interaction: discord.Interaction):
        save_interest(self.user_id, self.field)
        careers = recommend(self.field)

        if not careers:
            await interaction.response.send_message(
                "❌ No careers found for this field.",
                ephemeral=True
            )
            return

        msg = f"## {FIELDS[self.field]} {self.field.upper()} CAREERS\n\n"

        for c in careers:
            msg += (
                f"### {c['name']}\n"
                f"💰 Salary: {c['salary_tr']}\n"
                f"🧠 Skills: {', '.join(c['skills'])}\n"
                f"📄 {c['description']}\n\n"
            )

        await interaction.response.send_message(msg, ephemeral=True)


def get_field_view(user_id):
    view = View(timeout=60)
    for field in FIELDS:
        view.add_item(FieldButton(field, user_id))
    return view
