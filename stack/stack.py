"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from singly_linked_list import LinkedList

class Stack:
    # 1. Array
    # def __init__(self):
    #     self.size = 0
    #     self.storage = []

    # def __len__(self):
    #     return len(self.storage)

    # def push(self, value):
    #     return self.storage.append(value)

    # def pop(self):
    #     if len(self.storage) != 0:
    #         return self.storage.pop()
    #     else:
    #         return None

    # 2. Linked List
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.length

    def push(self, value):
        return self.storage.add_to_tail(value)

    def pop(self):
        return self.storage.remove_tail()
