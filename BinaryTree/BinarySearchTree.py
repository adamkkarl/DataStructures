#!/bin/python3

"""
Implementation of a basic binary search tree in python
"""

__author__ = "Adam Karl"

class BSTNode:
    def __init__(self, myData=None):
        self.data = myData
        self.left = None
        self.right = None
        
    def printTree(self):
        s = ''
        if self.left != None:
            s += self.left.printTree()
        s += str(self.data) + ', '
        if self.right != None:
            s += self.right.printTree()
        return s

    def insert(self, val):
        if val <= self.data:
            # insert to the left
            if self.left == None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        else:
            # insert to the right
            if self.right == None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)
                
    def search(self, val):
        if val == self.data:
            return True 
        elif val < self.data:
            if self.left == None:
                return False 
            else:
                return self.left.search(val)
        elif val > self.data:
            if self.right == None:
                return False 
            else:
                return self.right.search(val)

class BST:
    def __init__(self):
        self.head = None 

    def __str__(self):
        if self.head == None:
            return '[]'
        return '[' + self.head.printTree()[:-2] + ']'

    def insert(self, data):
        if self.head == None:
            self.head = BSTNode(data)
        else:
            self.head.insert(data)
            
    def search(self, val):
        if self.head == None:
            return False
        else:
            return self.head.search(val)
