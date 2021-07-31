class Roles:

    def __init__(self):
        super().__init__()
        self.roles = {}

    def add_role(self, role, actions=[]):
        """
        Add a role or add new roles with action types.
        """
        if not actions:
            raise Exception("Invalid Action Type")

        for action in actions:
            if action.upper() not in self.action_types:
                raise Exception("Invalid Action Type")

        self.roles.setdefault(role, set())
        self.roles[role].update(actions)

    def delete_role(self, user, role):
        """
        Delete a role for user.
        """
        assert not role or role in self.roles

        try:
            self.users[user].remove(role)
        except KeyError:
            print("Error: No role: {0} for user: {1}".format(
                role, user))
