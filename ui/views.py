import discord
from discord.ui import View, Button

class FieldSelectView(View):
    def __init__(self, callback):
        super().__init__(timeout=60)

        fields = [
            ("Technology", "technology", discord.ButtonStyle.primary),
            ("Creative", "creative", discord.ButtonStyle.success),
            ("Business", "business", discord.ButtonStyle.secondary)
        ]

        for label, value, style in fields:
            button = Button(label=label, style=style, custom_id=value)
            button.callback = callback
            self.add_item(button)
