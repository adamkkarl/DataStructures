#!/bin/python3

"""
Implementation of a singly linked list in python
"""

__author__ = "Adam Karl"

class Node:
    def __init__(self, myData=None):
        self.data = myData
        self.next = None

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
        
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            node.next = curr.next 
            curr.next = node
        self.size += 1
        
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
        