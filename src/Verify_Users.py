from User import User
from Read_Data import read_file, find_database
from Hash import HashTable

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

def put_users_in_group():
    """
    Reads the users from the database and puts them into the correct groups.

    Returns:
        dict: Returns a dictionary containing all the hashtables of groups.
    """
    data = read_file(find_database())
    users = get_users()

    # Get the number of different conversations in the database
    conversations = data.get("conversations", [])

    # Create a dictionary with a size equal to the number of conversations
    groups = dict()
    # Iterate through conversations and add users to the hash table
    for conversation in conversations:
        conversation_id = conversation.get("conversationID")
        participants = conversation.get("participants", [])
        groups[conversation_id] = HashTable(20, conversation_id)
         # Iterate through users and add them to the hash table if they are in the conversation
        for user in users:
            if user.get_id() in participants:
                groups[conversation_id].insert_user(user)
    return groups

def check_user_in_group(groups, group_name, user_id):
    """
    Checks if a user is in given hash table.

    Args:
        groups (_type_): The hash table containing the groups.
        group_name (_type_): The group name.
        user_id (_type_): The user id.

    Returns:
        bool: Returns True if the user is found and false otherwise.
    """
    return groups[group_name].check_id(user_id)
