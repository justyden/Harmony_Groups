''' An application that has common activites that make people happy. These activites are held in groups within the application and depending on the user that has signed in, they are allowed into the activites they belong to. These activites function as group chat for people that have similiar interest with these activites. The application uses a hash table to admit users into the specific group by verifying they belong to that activity.'''

from User import User
from GUIFrame import App
from Read_Data import read_file, find_database

def get_users():
    data = read_file(find_database())
    user_objects = [User(user_info["userName"], user_info["userID"]) for user_info in data.get("users", [])]
    return user_objects

def verify_user():
    return

users = get_users()
for user_obj in users:
    print(f"User Name: {user_obj.get_name()}, User ID: {user_obj.get_id()}")
