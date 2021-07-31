# roleBasedAccessControl
Implement a role based auth system. System is be able to assign a role to a user and remove a role from a user.

Please ignore .idea files as they are for project setup only.

Entities are USER, ACTION TYPE, RESOURCE, ROLE

ACTION TYPE defines the access level (For example: READ, WRITE, DELETE)

Access to resources for users are controlled strictly by the role. One user can have multiple roles. Given a user, action type and resource, the system is able to tell whether user has access or not.
