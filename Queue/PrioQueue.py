#!/bin/python3

"""
Implementation of a priority queue.
By default, a low priority value means a higher priority.
"""

__author__ = "Adam Karl"

class PrioQueue(object):
    def __init__(self, ascending=True):
        self.queue = list()
        self.ascending = ascending
        
    def __str__(self):
        if len(self.queue) == 0:
            return '[]'
        
        ret = '['
        for prio, data in self.queue:
            ret += f'({prio}, {data}), '
        return ret[:-2] + ']'
    
    def __len__(self):
        return len(self.queue)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def peek(self):
        """Look at the top item without dequeueing it"""
        if len(self.queue) == 0:
            return None 
        if self.ascending == True:
            return self.queue[0][1]
        else:
            return self.queue[-1][1]
    
    def enqueue(self, prio, data):
        i = 0
        while i < len(self.queue) and prio > self.queue[i][0]:
            i += 1
        self.queue.insert(i, [prio, data])
    
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        elif self.ascending == True: 
            ret = self.queue[0][1]
            del self.queue[0]
            return ret
        else:
            # non-default behavior, return highest value priority item
            ret = self.queue[-1][1]
            del self.queue[-1]
            return ret
