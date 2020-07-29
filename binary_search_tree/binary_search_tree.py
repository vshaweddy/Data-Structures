"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from singly_linked_list import LinkedList

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)
        # compare to the new value we want to insert

        if value < self.value:
            # if self.left is already taken by a node
                # make that node, call insert
            # set the left to the new node with the new value
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)


        if value >= self.value:
            # if self.right is already taken by a node
                #make that (right) node call insert
            # set the right child to the new node with the new value
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to the current value
        # if current value is more than the target:
        found = False
        if self.value >= target:
            # check the left subtree (self.left.contains(target))
            if self.left is None:
                return False
            found = self.left.contains(target)
            # if you cannot go left, return false

        # if current value is less than target
        if self.value <= target:
            # check if right subtree contains target
            # if you cannot go right, return False
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found

    # Return the maximum value found in the tree
    def get_max(self):
        # the largest value will always be to the right of the current node
        # if we can go right, let's find the largest nmber there by calling get_max on the right subtree
        if self.right is None:
             # if we cannot go right, return the current value
            return self.value
        max_value = self.right.get_max()
        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call function on the current value fn(self.value)
        fn(self.value)
        # if you can go left, call for_each on the right tree
        if self.left:
            self.left.for_each(fn)
        # if you can go right, call for_each on the right tree
        if self.right:
            self.right.for_each(fn)

    def in_order(self, fn):
        if self.left:
            self.left.in_order(fn)
        fn(self.value)
        if self.right:
            self.right.in_order(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        self.in_order(lambda x: print(x))   

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # create a queue for nodes
        queue = LinkedList()
        # add the first node to the queue
        queue.add_to_tail(self)
        # while queue is not empty
        while queue.length > 0:
            # remove the first node from the queue
            node = queue.remove_head()
            # print the removed node
            print(node.value)
            # add all children into the queue
            if node.left is not None:
                queue.add_to_tail(node.left)
            if node.right is not None:
                queue.add_to_tail(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # create a stack for nodes
        stack = []
        # add the first node to the stack
        stack.append(self)
        # while the stack is not empty
        while len(stack) > 0:
            # get the current node from the top of the stack
            node = stack.pop()
            # print that node
            print(node.value)
            # add all children to the stack
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
            # keep in the mind, the order you add the children, will matter (First In Last Out)
        
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
