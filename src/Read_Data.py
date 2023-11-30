'''This is a database reader class that will read the information from a text file.
This uses json to store and read information.'''

import json
import os

'''
# Example data
data = {
    "users": [
        {"userID": "user1", "userName": "John Doe"},
        {"userID": "user2", "userName": "Jane Doe"}
    ],
    "conversations": [
        {
            "conversationID": "group1",
            "participants": ["user1", "user2"],
            "messages": [
                {"sender": "user1", "text": "Hello, how are you?"},
                {"sender": "user2", "text": "I'm good, thanks!"}
            ]
        },
        {
            "conversationID": "group2",
            "participants": ["user1", "user3"],
            "messages": [
                {"sender": "user1", "text": "Hey there!"},
                {"sender": "user3", "text": "Hi, what's up?"}
            ]
        }
    ]
}
'''

# Find the Database.txt file
def find_database() -> object:
    locations_to_check = [
        "Database.txt",
        "src/Database.txt",
        "Harmony_Groups/src/Database.txt",
    ]

    for location in locations_to_check:
        try:
            # Attempt to check if the file exists at the current location
            if os.path.exists(location):
                return location

        except Exception as e:
            pass

    # If the loop completes without finding the file
    print("The location was of the database was not found. Please check the current directory and try again.")
    return None


# Write to the file
def update_file(file_name: str, data) -> None:
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)

# Read the existing data from the file
def read_file(file_name) -> object:
    with open(file_name, 'r') as file:
        file_content = file.read()
        if not file_content:
            data = {}
        else:
            data = json.loads(file_content)
        return data


def update_conversation(conversation: str, message: str, userID: str) -> None:
    file_name = find_database()
    data = read_file(file_name)
    conversation_to_update = next(
        (conv for conv in data["conversations"] if conv["conversationID"] == conversation),
        None
    )

    if conversation_to_update is not None:
        # Update the conversation, for example, add a new message
        new_message = {"sender": userID, "text": message}
        conversation_to_update["messages"].append(new_message)
    else:
        print(f"Conversation with ID {conversation} not found.")
    update_file(file_name, data)

'''Here is an example of how to use these function together
update_conversation("Database.txt", "group1", "This is awesome.", "user1")
'''