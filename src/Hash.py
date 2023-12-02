from LinkedList import LinkedList
from User import User
import random
import string

# The examle UserId I used was a12b34c56 so basically
# (char)(num)(num)(char)(num)(num)(char)(num)(num)

"""
HashTable class that represents a Hash Table data structure.
Each HashTable object represents a LinkedList object. The Nodes
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
    def __init__(self, size, group):
        """
        Constructs HashTable object with a size and a list

        Args:
             size (int): the size of the HashTable list
        """
        self.size = size
        self.table = [LinkedList() for i in range(size)]  # The hash table (a list), stores LinkedList objects at each index
        self.group = group

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

    def insert_user(self, user):
        """
        Inserts a User object into the LinkedList object at the given HashTable index

        Args:
            user (User): the User object to be placed in the LinkedList
        """
        hash = self.custom_hash(str(user.get_id()))
        index = self.calc_index(hash)
        self.table[index].insert(user)  # Inserts User object in the LinkedList at the specified index

    def print_table(self):
        """
        Prints out the HashTable
        """
        for i in range(self.size):
            self.table[i].display()  # Calls each LinkedList object's display() function
            
    def check_id(self, user_id):
        """
        Checks if the LinkedList object at the specified index in the HashTable is empty

        Args:
            index (int): the index of the HashTable

        Returns:
            bool: True if the linked list is empty, False otherwise
        """
        hash = self.custom_hash(str(user_id))
        spot = self.calc_index(hash)
        if self.table[spot].is_empty():
            return False
        else:
            return self.table[spot].search_user_by_id(str(user_id))
        
    def get_group(self):
        return self.get_group