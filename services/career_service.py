import json

class CareerService:
    def __init__(self):
        with open("data/careers.json", encoding="utf-8") as f:
            self.data = json.load(f)

    def get_careers(self, field):
        return self.data[field]["careers"]

    def get_title(self, field):
        return self.data[field]["title"]
