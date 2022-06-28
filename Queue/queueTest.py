#!/bin/python3

"""
Test the implementation of Queues in this directory
"""

__author__ = "Adam Karl"

import random
import Queue, PrioQueue

def testQueue():
    """test the queue implementation"""
    print("Testing Queue: items should print in increasing magnitude", flush=True)
    q = Queue.Queue()
    for i in range(20):
        q.enqueue(i)
    
    while q.isEmpty() == False:
        val = q.dequeue()
        print(f"{val} ", end='')
    print('\n')

def testPrioQueue():
    """test the priority queue implementation"""
    print("Testing Priority Queue")
    print("Increasing Priority Queue: items should print in increasing magnitude", flush=True)
    pq = PrioQueue.PrioQueue()
    for _ in range(20):
        rand = random.randint(0,99)
        pq.enqueue(rand, rand)
        
    while pq.isEmpty() == False:
        val = pq.dequeue()
        print(f"{val} ", end='')
    print()
    
    print("Decreasing Priority Queue: items should print in decreasing magnitude", flush=True)
    pq = PrioQueue.PrioQueue(ascending=False)
    for _ in range(20):
        rand = random.randint(0,99)
        pq.enqueue(rand, rand)

    while pq.isEmpty() == False:
        val = pq.dequeue()
        print(f"{val} ", end='')
    print('\n')

def main():    
    testQueue()
    testPrioQueue()

if __name__ == "__main__":
    main()