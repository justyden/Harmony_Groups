'''
User class that represents a user in a group chat.
Users will have a Name to be identified in a group chat,
and an ID which identifies which groups they have access
to.
'''
class User:
    """
    The User class for creating unique User objects.

    Attributes:
        name: str
        id: str
    """

    def __init__(self, name, id) -> None:
        """
        Initializes User object with a name and id

        Args:
        name (str): The user's name
        id (str):  The user's account ID
        """
        self.name = name
        self.id = id

    def get_name(self) -> str:
        """
        Gets the name of the User instance

        Returns:
            str: A string that represents the user's name
        """
        return self.name

    def get_id(self) -> str:
        """
        Gets the ID of the User instance

        Returns:
            str: A string that represents the user's ID
        """
        return self.id

    def __str__(self):
        """
        Returns the name of the User object when printed

        Returns:
             str: User object's name value
        """
        return self.id
