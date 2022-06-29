#!/bin/python3

"""
Test the implementation of binary trees this directory
"""

__author__ = "Adam Karl"

import random
import BinarySearchTree

def testBST():
    """test the binary search tree implementation"""
    print("Testing Binary Search Tree", flush=True)
    
    bst = BinarySearchTree.BST()
    for _ in range(50):
        bst.insert(random.randint(0,99))
        
    print(bst)
        
    for _ in range(10):
        n = random.randint(0,99)
        if bst.search(n):
            print(f"{n} IS in bst")
        else:
            print(f"{n} IS NOT in bst")

def main():    
    testBST()
    
if __name__ == "__main__":
    main()