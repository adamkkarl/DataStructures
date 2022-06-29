#!/bin/python3

"""
Test the implementation of Linked Lists in this directory
"""

__author__ = "Adam Karl"

import SinglyLinkedList, DoublyLinkedList

def testSinglyLinkedList():
    """test the singly linked list implementation"""
    print("Testing Singly Linked List: items should print in alphabetical order", flush=True)
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
    print('\n')
    
def testDoublyLinkedList():
    """test the doubly linked list implementation"""
    print("Testing Doubly Linked List: items should print in alphabetical order", flush=True)
    DLL = DoublyLinkedList.LinkedList()
    DLL.insert('d')
    DLL.push('b')
    DLL.insert('c', 1)
    DLL.insert('a')
    DLL.insert('e', 4)
    
    print(DLL)
    
    # print(DLL.pop(4)) # pop the last element
    
    while len(DLL) > 0:
        print(DLL.pop(), end='')
    print('\n')


def main():    
    testSinglyLinkedList()
    testDoublyLinkedList()

if __name__ == "__main__":
    main()