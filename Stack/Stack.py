#!/bin/python3

"""
Implementation of a generic stack LIFO data structure
This file is mainly for reference since standard python lists
can already function as stacks.
"""

__author__ = "Adam Karl"

class Stack(object):
    def __init__(self):
        self.stack = list()
        
    def __str__(self):
        if len(self.stack) == 0:
            return '[]'
        
        ret = '['
        for item in self.stack:
            ret += f'{item}, '
        return ret[:-2] + ']'
    
    def __len__(self):
        return len(self.stack)
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def peek(self):
        """Look at the top item without popping it"""
        if len(self.stack) == 0:
            return None 
        return self.stack[-1]
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    