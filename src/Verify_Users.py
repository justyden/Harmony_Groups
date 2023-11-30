from User import User
from Read_Data import read_file, find_database

def get_users():
    """
    Create user objects from the database.

    Returns:
        list(user)
    """
    data = read_file(find_database())
    user_objects = [User(user_info["userName"], user_info["userID"]) for user_info in data.get("users", [])]
    return user_objects

def check_user_in_list(input_name, input_id):
    user_objects = get_users()
    """
    Check if a user with the given name and ID is in the list of User objects.

    Args:
        input_name (str): Name to check.
        input_id (str): ID to check.

    Returns:
        bool: True if the user is in the list, False otherwise.
    """
    for user in user_objects:
        if user.get_name() == input_name and user.get_id() == input_id:
            return True
    return False

