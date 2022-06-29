#!/bin/python3

"""
Test the implementation of Linked Lists in this directory
"""

__author__ = "Adam Karl"

import SinglyLinkedList

def testSinglyLinkedList():
    """test the singly linked list implementation"""
    print("Testing Singly Linked List: items should print in increasing magnitude", flush=True)
    SLL = SinglyLinkedList.LinkedList()
    SLL.insert('d')
    SLL.insert('b')
    SLL.insert('c', 1)
    SLL.insert('a')
    SLL.insert('e', 4)
    
    print(SLL)
    
    # print(SLL.pop(4)) # pop the last element
    
    while len(SLL) > 0:
        print(SLL.pop(), end='')
    print()

def main():    
    testSinglyLinkedList()

if __name__ == "__main__":
    main()