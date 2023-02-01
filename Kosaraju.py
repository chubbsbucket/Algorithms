# Kosaraju's algorithm for finding strongly-connected components in a graph

from collections import defaultdict
import copy
class graph:

    def __init__ (self):
        self.vertices = {}

    def reverse(self):

        revGraph = graph()

        for vertice in self.vertices.keys():
            revGraph.vertices[vertice] = []

        for vertice in self.vertices.keys():
            for i in self.vertices[vertice]:
                revGraph.vertices[i].append(vertice)

        return revGraph

    def printgraph(self):
        print(self.vertices)

def DFS(Graph, start, dictExplore, Finish, leader, FirstPass):
    stack = []
    stack.append((start, 0))


    while bool(stack):
        (vertex, index) = stack[-1]

        if index == 0:
            dictExplore[vertex] = 0

        stack.pop()
        stack.append((vertex, index + 1))

        if vertex in Graph.vertices:
            if index < len(Graph.vertices[vertex]):
                edge = Graph.vertices[vertex][index]

                if not (edge in dictExplore.keys()):
                    stack.append((edge, 0))
                continue

            if FirstPass == True:
                global t
                t += 1
                Finish[t] = vertex

            elif FirstPass == False:
                if start not in leader.keys():
                    leader[s] = []

                leader[s].append(vertex)

            stack.pop()



def DFSLoop(Grev, G, nodeNumber):

    global t
    t = 0

    Finish = [0] * (nodeNumber + 1)

    dictExplore = {}
    leader = {}

    v = nodeNumber

    while v > 0:

        if v not in dictExplore.keys():
            DFS(Grev, v, dictExplore, Finish, leader, True)

        v -= 1

    dictExplore = {}

    i = nodeNumber
    while i != 0:
        vert = Finish[i]

        if vert not in dictExplore.keys():
            global s
            s = vert
            DFS(G, vert, dictExplore, Finish, leader, False)

        i -= 1


    SCCs = []
    maxSCC = []

    for lead in leader.keys():
        SCCs.append(len(leader[lead]))

    while len(SCCs) > 0 and len(maxSCC) < 5:

        x = max(SCCs)
        maxSCC.append(x)
        SCCs.remove(x)

    while len(maxSCC) < 5:
        maxSCC.append(0)

    maxSCC.sort(reverse = True)
    print(maxSCC)

Graph1 = graph()

file = input("Filename:")
nodeNumber = int(input("Nodes:"))

with open(file) as f:
    lines = f.readlines()
f.close()

for i in range(1, nodeNumber + 1, 1):
    Graph1.vertices[i] = []

for line in lines:
    x = line.split()
    x = list(map(lambda y: int(y), x))
    Graph1.vertices[x[0]].extend(x[1:])

Grev = Graph1.reverse()

DFSLoop(Grev, Graph1, nodeNumber)