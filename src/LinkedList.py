"""
Node class that represents individual user in the
linked list.
"""
class Node:
    """
    Node class meant to store users in the linked list.

    Attributes:
        val: str
        next: Node
        prev: Node
    """
    def __init__(self, val):
        """
        Node class constructor

        Args:
            val: A user ID
        """
        self.val = val
        self.next = None  # The node following the current node
        self.prev = None  # The node behind the current node


"""
LinkedList class that builds a linked list out of
Node objects.
"""
class LinkedList:
    """
    LinkedList class designed to construct a linked list

    Attributes:
        head: Node
        last: Node
    """
    def __init__(self):
        """
        LinkedList class constructor
        """
        self.head = None  # Head is the first Node in the list
        self.last = None  # Last is the last Node in the list

    def insert(self, val):
        """
        Inserts a new user Node at the end of the LinkedList. Similar to an 'append()' function.

        Args:
            val (Node): A Node object that describes a user
        """
        if self.head == None:
            self.head = Node(val)
            self.last = self.head  # When only one node is in the LinkedList, it's both the head and last node
        else:
            temp = self.last  # Temporarily stores self.last's value to set self.last.prev's value
            self.last.next = Node(val)
            self.last = self.last.next
            self.last.prev = temp

    def display(self):
        """
        Prints all Nodes in the LinkedList
        """
        current = self.head  # current is a variable used to iterate through the LinkedList
        while current is not None:
            # print(current.val, "\n", end=" ")  # NOTE: might be a solution
            print(current.val, end=" ")  # NOTE: prints each individual LinkedList on same line
            current = current.next  # Changes current's value to the next Node in the list
        print()  # Used to create a new line for printing all LinkedList objects

    def remove(self, user):
        """
        Removes the specified user Node from the LinkedList

        Args:
            user (str): A string that represents the userID to be removed from the LinkedList
        """
        current = self.head
        if self.head.val == user:  # If the Node to delete is the head Node
            self.head = self.head.next  # Move self.head up to the next Node
            self.head.prev = None  # Set the new self.head's prev position to None
        elif self.last.val == user:  # If Node to delete is the last Node
            self.last = self.last.prev  # Move self.last back to the prev Node
            self.last.next = None  # Set the new self.last's next to None
        else:
            while current.next:  # Iterate over LinkedList to find the Node to remove
                if current.val == user:  # Checks if the current Node matches the Node to be removed
                    current.prev.next = current.next  # For the Node behind current, set its next value to current.next
                    current.next.prev = current.prev  # For the Node ahead of current, set its prev value to current.prev
                current = current.next


    def search_user_by_id(self, user_id):
        """
        Searches the linked list for a user with a specified user ID

        Args:
            user_id (str): The user ID to search for

        Returns:
            bool: True if a user with the specified ID is found, False otherwise.
        """
        current = self.head
        while current:
            if current.val.get_id() == user_id:
                return True  # User found
            current = current.next
        return False  # User not found

    def is_empty(self):
        """
        Checks if the linked list is empty

        Returns:
            bool: True if the linked list is empty, False otherwise
        """
        return self.head is None
