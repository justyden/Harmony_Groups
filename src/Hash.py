from LinkedList import LinkedList
from User import User
import random
import string

"""
HashTable class that represents a Hash Table data structure.
Each element of the HashTable object will hold a LinkedList object,
representing an activity (e.g. Swimming) group chat. The Nodes
in the LinkedList objects represent User objects part of the
activity group chat.
"""
class HashTable:
    """
    The HashTable class for creating a Hash Table object

    Attributes:
        size: int
        table: List
    """
    def __init__(self, size):
        """
        Constructs HashTable object with a size and a list

        Args:
             size (int): the size of the HashTable list
        """
        self.size = size
        self.table = [LinkedList() for i in range(size)]  # The hash table (a list), stores LinkedList objects at each index

    def custom_hash(self, input_string):
        """
        Creates a hash code for a User's id

        Args:
            input_string (str): a User object's id value

        Returns:
            int: the hash code value generated from the hash function
        """
        hash_value = 5381  # a prime number

        for char in input_string:
            # Multiply the current hash value by 31 and add the ASCII value of the character
            hash_value = (hash_value * 31) + ord(char)  # ord(char) returns the Unicode value of a character

        return hash_value

    def calc_index(self, hash_code):
        """
        Calculates the index of the HashTable the object should be placed in based on its hash code

        Args:
            hash_code (int): the hash code of the User object's id value

        Returns:
            int: the index of the hash table to place the object
        """
        index = hash_code % self.size  # Calculates the index based on the size of the array
        return index

    def insert_user(self, user, index):
        """
        Inserts a User object into the LinkedList object at the given HashTable index

        Args:
            user (User): the User object to be placed in the LinkedList
        """
        self.table[index].insert(user)  # Inserts User object in the LinkedList at the specified index

    def pick_name(self):
        """
        Picks a random name when creating a User object

        Returns:
             str: a name from the names[] list for a User object
        """
        names = ["James", "Mary", "Robert", "Jennifer", "Michael", "Susan", "Richard", "Lisa", "Daniel", "Nicole",
                 "Justin", "Sarah", "Anthony", "Ashley", "Steven", "Emily", "Kevin", "Amanda", "Jason", "Laura"]
        return random.choice(names)  # Selects and returns random name from the list

    def pick_id(self):
        """
        Randomly generates a User id when creating a User object

        Returns:
            str: an id for a User object
        """
        letters = string.ascii_lowercase  # Creates a list of lowercase letters
        identifier = ""  # Variable to store the newly created User id
        switch = False  #  Variable to alternate between picking a letter or number
        for i in range(6):
            if not switch:
               identifier  += random.choice(letters)  # Appends random letter
               switch = True
            else:
                identifier += str(random.randint(10,99))  # Appends random number
                switch = False
        return identifier

    def print_table(self):
        """
        Prints out the HashTable
        """
        for i in range(self.size):
            self.table[i].display()  # Calls each LinkedList object's display() function

if __name__ == "__main__":
    h = HashTable(4)  # Example HashTable with size 4 for 4 different activities
    users = []  # List to store randomly generated User objects
    for i in range(3):
        name = h.pick_name()
        ID = h.pick_id()
        users.append(User(name,ID))  # Creates new User object and appends it to users list

    for u in users:
        print("user:",u)  # Displays randomly created User objects
        hash = h.custom_hash(u.id)
        index = h.calc_index(hash)
        h.insert_user(u, index)  # Inserts User objects into positions based on their hash code

    h.print_table()  # Prints the HashTable