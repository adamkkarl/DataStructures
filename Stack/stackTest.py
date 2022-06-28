#!/bin/python3

"""
Test the implementation of Stack in this directory
"""

__author__ = "Adam Karl"

import Stack

def testStack():
    """test the stack implementation"""
    print("Testing Stack: items should print in decreasing magnitude", flush=True)
    s = Stack.Stack()
    for i in range(20):
        s.push(i)
        
    # print(s)
    
    while s.isEmpty() == False:
        val = s.pop()
        print(f"{val} ", end='')
    print('\n')

def main():    
    testStack()

if __name__ == "__main__":
    main()