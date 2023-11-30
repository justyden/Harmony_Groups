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
    data = read_file(find_database())
    users = get_users()

    # Get the number of different conversations in the database
    conversations = data.get("conversations", [])
    num_conversations = len(conversations)

    # Create a HashTable with a size equal to the number of conversations
    hash_table = HashTable(size=num_conversations)

    # Iterate through conversations and add users to the hash table
    for conversation in conversations:
        conversation_id = conversation.get("conversationID")
        participants = conversation.get("participants", [])

        # Iterate through users and add them to the hash table if they are in the conversation
        for user in users:
            if user.get_id() in participants:
                hash_code = hash_table.custom_hash(user.get_id())
                index = hash_table.calc_index(hash_code)
                hash_table.insert_user(user, index)
                
    return hash_table

def check_user_in_group(input_id):
    return

if __name__ == "__main__":
    # Example usage:
    user_hash_table = put_users_in_group()
    user_hash_table.print_table()