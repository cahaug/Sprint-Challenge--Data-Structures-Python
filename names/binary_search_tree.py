import sys

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None #BinarySearchTree
        self.right = None  #BinarySearchTree

    # Insert the given value into the tree
    def insert(self, value):        
        if value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
            return
        elif value >= self.value and self.right is None:
            self.right  = BinarySearchTree(value)
            return
        
        if value < self.value:
            self.left.insert(value)
        else:
            self.right.insert(value)
        # compare value to the current node
        # if smaller, go left
        # if larger, go right
        # if no node to go to, ie left or right is none
        # make a new node at that spot
        # pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # base case
        if target == self.value:
            return True
        # recursive cases
        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        # compare value to the current node value
        # if smaller, go left
        # if larger, go right
        # if equal, return True

        # if smaller, but we can't go left, return false
        # if larger, but we can't go right, return false


    # Return the maximum value found in the tree
    def get_max(self):
        # until right = none go right, return the final value
        if self.right is None:
            return self.value
        return self.right.get_max()
        # while self.right is not None:
        #     self = self.right
        # return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)
        # if self.left:
        #     self.left.for_each(cb)
        # if self.right:
        #     self.right.for_each(cb)
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # go left first
        if self.left:
        # if self.left is not None:
            self.left.in_order_print(node.left)
        #print ourselves
        print(node.value)

        # go right
        if self.right:
        # if self.right is not None:
            self.right.in_order_print(node.right)