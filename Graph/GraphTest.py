#!/bin/python3

"""
Test the implementation of Graphs in this directory
"""

__author__ = "Adam Karl"

import Graph

def testGraph():
    """test the graph implementation"""
    print("Testing Graph:\n", flush=True)
    
    g = Graph.Graph()
    g.addVertex('a')
    g.addEdge('a','b')
    g.addEdge('c','d')
    g.addDirectedEdge('a','e')
    
    print(g)


def main():    
    testGraph()

if __name__ == "__main__":
    main()