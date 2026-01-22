import json

class CareerService:
    def __init__(self):
        with open("data/careers.json", encoding="utf-8") as f:
            self.data = json.load(f)

    def get_fields(self):
        return self.data.keys()

    def get_field(self, field):
        return self.data[field]

    def format_careers(self, field, level):
        field_data = self.data[field]
        result = f"**{field_data['title']}**\n\n"

        for career in field_data["careers"]:
            result += f"### {career['name']}\n"
            result += f"**Skills:** {', '.join(career['skills'])}\n"
            result += f"**Education:** {career['education']}\n"
            result += f"**Salary ({level.title()}):** {career['salary'][level]}\n\n"

        return result
