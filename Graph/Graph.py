#!/bin/python3

"""
Implementation of a Graph in python
"""

__author__ = "Adam Karl"

class Graph:
    def __init__(self, dict=None):
        if dict is None:
            dict = {}
        self.graph_dict = dict 

    def __str__(self):
        ret = 'source: destination\n'
        for v in self.graph_dict.keys():
            ret += v + ': '
            for c in self.getConnections(v):
                ret += c + ' '
            ret += '\n'
        return ret

    def addVertex(self, v):
        if v not in self.graph_dict:
            self.graph_dict[v] = []
            
    def getVertices(self):
        return self.graph_dict.keys()

    def addEdge(self, v0, v1):
        """Add undirected edge between 2 vertices"""
        self.addVertex(v0)
        self.addVertex(v1)
        self.graph_dict[v0].append(v1)
        self.graph_dict[v1].append(v0)
        
    def addDirectedEdge(self, v0, v1):
        """Add directed edge from 1 vertex to another"""
        self.addVertex(v0)
        self.addVertex(v1)
        self.graph_dict[v0].append(v1)

    def getConnections(self, v):
        # return all vertices connected to this one
        return self.graph_dict[v]
