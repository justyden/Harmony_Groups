'''
This is an example hash function from ChatGPT.
The examle UserId I used was a12b34c56 so basically
(char)(num)(num)(char)(num)(num)(char)(num)(num)
'''
from src.linked_list import LinkedList


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
        #index = hash_code % array_size
        index = hash_code % self.size
        return index


    def print_table(self):
        for i in range(self.size):
            self.table[i].insert(i)
            self.table[i].display()

# hash_table = [1,2,3,4,5,6,7,8,9,10,11,12,13] # filling example hash_table list to give it a length to test calc_index()
# array_size = len(hash_table)





# hash_value = custom_hash("a12b34c56")
# print(hash_value)
#
# index = calc_index(hash_value)
# print(index)

h = HashTable(3)
h.print_table()