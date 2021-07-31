from roleManagement.acl import Registry
from roleManagement.constants import READ, WRITE, DELETE,\
    SUPER_USER, ADMIN, NON_ADMIN, FILES, DOCUMENTS

ACCESS_LEVELS = {
    SUPER_USER: [READ, WRITE, DELETE],
    ADMIN: [READ, WRITE],
    NON_ADMIN: [READ]
}

RESOURCES = [FILES]


class RBAC:
    """
    Implements Role Based Access Control.
    System should be able to assign a role to user and remove
    a user from the role.
    """

    def __init__(self):
        self.acl = Registry()

    def add_role(self):
        """
        Adds roles available in ACCESS_LEVELS.
        """
        for role, access_levels in ACCESS_LEVELS.items():
            self.acl.add_role(role, access_levels)

    def add_resource(self):
        """
        Adds Resources available in RESOURCES.
        """
        for resource in RESOURCES:
            self.acl.add_resource(resource)

    def allow_rule(self):
        """
        Implements allow rules.
        """
        for role, access_levels in ACCESS_LEVELS.items():
            for acl in access_levels:
                self.acl.allow(role, acl, RESOURCES)

    def deny_role(self):
        """
        Implements Deny roles.
        """
        for role, access_levels in ACCESS_LEVELS.items():
            for acl in ACCESS_LEVELS[SUPER_USER]:
                if acl not in access_levels:
                    self.acl.deny(role, acl, RESOURCES)

    def add_users(self):
        """
        Add users with roles.
        """
        self.acl.add_user('kanvi', [NON_ADMIN, ADMIN])
        self.acl.add_user('kanvi', [SUPER_USER])

    def perform_operations(self):
        """
        To Check Permission
        """
        self.acl.is_allowed('kanvi', READ, FILES)
        self.acl.is_allowed('kanvi', WRITE, FILES)


if __name__ == "__main__":
    # These need to be called using command line operations
    rbac = RBAC()
    rbac.add_role()
    rbac.add_resource()
    rbac.allow_rule()
    rbac.deny_role()
    rbac.add_users()
    rbac.perform_operations()
