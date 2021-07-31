class Users:

    def __init__(self):
        super().__init__()
        self.users = {}

    def add_user(self, user, roles=[]):
        """
        Add a user with role.
        """
        for role in roles:
            assert not role or role in self.roles

        self.users.setdefault(user, set())
        self.users[user].update(roles)
