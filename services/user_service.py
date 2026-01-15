class UserService:
    def __init__(self):
        self.users = {}

    def set_interest(self, user_id, field):
        self.users[user_id] = field

    def get_interest(self, user_id):
        return self.users.get(user_id)
