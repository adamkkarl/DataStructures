#!/bin/python3

"""
Implementation of a generic queue in python
"""

__author__ = "Adam Karl"

class Queue(object):
    def __init__(self):
        self.queue = list()
        
    def __str__(self):
        if len(self.queue) == 0:
            return '[]'
        
        ret = '['
        for item in self.queue:
            ret += f'{item}, '
        return ret[:-2] + ']'
    
    def __len__(self):
        return len(self.queue)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def peek(self):
        """Look at the top item without dequeueing it"""
        if len(self.queue) == 0:
            return None 
        return self.queue[0]
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        item = self.queue[0]
        del self.queue[0]
        return item
    