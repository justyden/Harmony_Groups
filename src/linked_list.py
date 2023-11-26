class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    # For inserting a new user into the LinkedList
    def insert(self, val):
        # current is a variable used to traverse the linked list
        if self.head == None:
            self.head = Node(val)
            self.last = self.head
        else:
            temp = self.last
            self.last.next = Node(val)
            self.last = self.last.next
            self.last.prev = temp

    def display(self):
        current = self.head
        while current is not None:
            print(current.val, end=" ")
            current = current.next

    def display_last(self):
        print(self.last.val)



    # For removing a user from the LinkedList
    def remove(self, user):
        current = self.head
        # if the node to delete is the head node
        if self.head.val == user:
            # move self.head up to the next node
            self.head = self.head.next
            # set the new self.head's prev position to None
            self.head.prev = None
        # if node to delete is the last node
        elif self.last.val == user:
            # move self.last back to the prev node
            self.last = self.last.prev
            # set the new self.last's next to None
            self.last.next = None
        else:
            # iterate over nodes to find the node to remove from list
            while current.next:
                # checks if the current node matches the node to be removed
                if current.val == user:
                    # for the node behind the current node, set its next value to current.next
                    current.prev.next = current.next
                    # for the node ahead of current, set its prev value to current.prev
                    current.next.prev = current.prev
                current = current.next


user1 = "a"
user2 = "b"
user3 = "c"
user4 = "d"
LL1 = LinkedList()
LL1.insert(user1)
LL1.insert(user2)
LL1.insert(user3)
LL1.insert(user4)
LL1.display()
print()


LL1.remove("b")
print()
LL1.display()
# print()
# LL1.display_last()
