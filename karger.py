# implementation of Karger's algorithm

import math
import copy
import random

class graph:
    def __init__ (self):
        self.vertices = {}

    def addVertexWithEdges(self, list1):
        self.vertices[list1[0]] = list1[1:]

    def mergeVertices(self, edge):
        v1 = edge[0]
        v2 = edge[1]
        
        self.vertices[v1].extend(self.vertices[v2])
        del self.vertices[v2]
        for k in list(self.vertices.keys()):
            self.vertices[k] = [v1 if x == v2 else x for x in self.vertices[k]]
        
        self.vertices[v1] = [x for x in self.vertices[v1] if x != v1]
        
       
    def printGraph(self):
        print(self.vertices)

def Karger(Graph):

    vert = len(Graph.vertices)
    while vert > 2:
        limit = len(Graph.vertices)
        index1 = random.randint(0, limit - 1)
        v1 = list(Graph.vertices.keys())[index1]
        vertlist = len(Graph.vertices[v1])
        index2 = random.randint(0, vertlist - 1)
        v2 = Graph.vertices[v1][index2]
        edge = (v1, v2)
        Graph.mergeVertices(edge)
        vert = len(Graph.vertices)
    
    mincut = len(Graph.vertices[list(Graph.vertices.keys())[0]])
    return mincut

if __name__ == "__main__":

    filename = input("graph:")
    with open(filename) as f:
        lines = f.readlines()
    f.close()

    Graph = graph()
    
    for line in lines:
        g = line.split()
        g = list(map(lambda y: int(y), g))
        Graph.addVertexWithEdges(g)

    n = len(Graph.vertices)
    
    Graph1 = copy.deepcopy(Graph)
    
    x = Karger(Graph1)
    
    i = 0
    while i < 20 * n:
        Graph1 = copy.deepcopy(Graph)
        y = Karger(Graph1)
        if y < x:
            x = y
        i += 1
    
    print(x)