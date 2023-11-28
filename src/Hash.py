'''
This is an example hash function from ChatGPT.
The examle UserId I used was a12b34c56 so basically
(char)(num)(num)(char)(num)(num)(char)(num)(num)
'''
from src.linked_list import LinkedList
import random
import string
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
        return self.name


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [LinkedList() for i in range(size)]  # add linkedlist objects to each index in the array

    def custom_hash(self, input_string):
        hash_value = 5381  # a prime number

        for char in input_string:
            # Multiply the current hash value by 31 and add the ASCII value of the character
            hash_value = (hash_value * 31) + ord(char)  # ord(char) returns the Unicode value of a character

        return hash_value

    def calc_index(self, hash_code):
        index = hash_code % self.size
        return index

    def insert_user(self, user, index):
        self.table[index].insert(user)  # Inserts user object in the LinkedList at the specified index

    def pick_name(self):
        names = ["James", "Mary", "Robert", "Jennifer", "Michael", "Susan", "Richard", "Lisa", "Daniel", "Nicole",
                 "Justin", "Sarah", "Anthony", "Ashley", "Steven", "Emily", "Kevin", "Amanda", "Jason", "Laura"]
        return random.choice(names)

    def pick_id(self):
        letters = string.ascii_lowercase
        identifier = ""
        switch = False
        for i in range(6):
            if not switch:
               identifier  += random.choice(letters)
               switch = True
            else:
                identifier += str(random.randint(10,99))
                switch = False
        return identifier



    def print_table(self):
        for i in range(self.size):
            self.table[i].display()


u1 = User("Sam", "a12b34c56")
u2 = User("Greg", "a12b34c56")
u3 = User("Tom", "a12b34c56")
u4 = User("Rick", "x29y81z76")

h = HashTable(4)
# #h.print_table()
# hash1 = h.custom_hash(u1.id)
# # print(hash1)
# index1 = h.calc_index(hash1)
# # print(index1)
# h.insert_user(u1, index1)
# # print("checking output")
# # h.check_table()
#
# hash2 = h.custom_hash(u2.id)
# # print(hash2)
# index2 = h.calc_index(hash2)
# # print(index2)
# h.insert_user(u2, index2)
# # print("checking output")
# # h.check_table()
#
# hash3 = h.custom_hash(u3.id)
# # print(hash2)
# index3 = h.calc_index(hash3)
# # print(index2)
# h.insert_user(u3, index3)
# # print("checking output")
# # h.check_table()
#
# hash4 = h.custom_hash(u4.id)
# print(hash4)
# index4 = h.calc_index(hash4)
# print(index4)
# h.insert_user(u4, index4)
# print("checking output")
# h.print_table()

#print(h.pick_id())

users = []
for i in range(3):
    name = h.pick_name()
    ID = h.pick_id()
    users.append(User(name,ID))

print("going to print user array")
for u in users:
    print("user:",u)
    hash = h.custom_hash(u.id)
    index = h.calc_index(hash)
    h.insert_user(u, index)
    #print(u)
h.print_table()