#!/bin/python3

"""
Implementation of a doubly linked list
Current implementation doesn't take advantage of the doubly-linked structure,
would need to be expanded/modified based on usage
"""

__author__ = "Adam Karl"

class Node:
    def __init__(self, myData=None):
        self.data = myData
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def __str__(self):
        if self.size == 0:
            return '[]'
        
        ret = '['
        curr = self.head
        while curr != None:
            ret += f'{curr.data}, '
            curr = curr.next
        return ret[:-2] + ']'
    
    def __len__(self):
        return self.size
    
    def insert(self, data, index=0):
        node = Node(data)
        if self.size == 0:
            # add the first item to the list
            self.head = node
        elif index == 0:
            # add at beginning of list
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next            
            node.next = curr.next
            curr.next = node 
        self.size += 1
        
    def push(self, data):
        """add to head"""
        self.insert(data, 0)
        
    def pop(self, index=0):
        ret = None
        if index == 0:
            ret = self.head.data
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index-1):
                 curr = curr.next 
            ret = curr.next.data
            curr.next = curr.next.next

        self.size -= 1
        return ret
        