
class Resources:
    """
    Implements addResource to add the resources.
    """

    def __init__(self):
        self.resources = {}

    def add_resource(self, resource, parents=[]):
        """
        Add a resource or append resource.
        """
        self.resources.setdefault(resource, set())
        self.resources[resource].update(parents)
