#Dijkstra's algorithm implemented using a heap

import heapq
import itertools
class graph:
        def __init__ (self):

                self.vertices = {}

        def loadGraph(self, file):
                with open(file) as f:
                        lines = f.readlines()

                f.close()

                for line in lines:
                        line = line.split()
                        v = int(line[0])
                        self.vertices[v] = []
                        i = 1
                        while i < len(line):
                                pair = line[i].split(",")
                                (edge, length) = (int(pair[0]), int(pair[1]))
                                self.vertices[v].append((edge, length))
                                i = i + 1
        def printGraph(self):
                print(self.vertices)

class Heap:
        def __init__ (self):
                self.heap = []
                self.entry_finder = {}
                self.counter = itertools.count()

        def remove_task(self, vertex):
                self.entry_finder[vertex] = False
        def add_task(self, vertex, key):
                # you don't actually modify an entry in the heap, as this would compromise the structure of the heap. Instead, you just keep track of the correct entry in entry_finder.
                if vertex in self.entry_finder:
                        self.remove_task(vertex)
                count = next(self.counter)
                entry = [key, count, vertex]
                self.entry_finder[vertex] = entry
                heapq.heappush(self.heap, entry)
        def pop_task(self):
                while self.heap:
                        key, count, vertex = heapq.heappop(self.heap)
                        # if the vertex is already explored, ignore it when it comes up in the heap by this if statement.
                        if self.entry_finder[vertex] == False:
                                continue
                        # check if your entry is the correct one
                        elif [key, count, vertex] == self.entry_finder[vertex]:
                                self.remove_task(vertex)
                                return [key, count, vertex]

def dijkstra(graph):
        lenGraph = len(graph.vertices.keys())
        dictExplore = {}
        A = [1000000] * (lenGraph + 1)
        exploredNodes = 1
        heap = Heap()

        A[1] = 0


        for i in range(1, lenGraph + 1):
                dictExplore[i] = False

        dictExplore[1] = True

        shortest = {}
        for (v, length) in graph.vertices[1]:

                if dictExplore[v] == False:
                        if v not in shortest.keys():
                                shortest[v] = length
                        elif length < shortest[v]:
                                shortest[v] = length

        for v in shortest:
                newKey = A[1] + shortest[v]
                heap.add_task(v, newKey)


        while exploredNodes < lenGraph:

                exploredNodes += 1

                infoList = heap.pop_task()

                dictExplore[infoList[2]] = True

                A[infoList[2]] = infoList[0]

                shortest = {}
                for (v, length) in graph.vertices[infoList[2]]:

                        if dictExplore[v] == False:
                                if v not in shortest.keys():
                                        shortest[v] = length
                                elif length < shortest[v]:
                                        shortest[v] = length

                for v in shortest:
                        if v in heap.entry_finder:
                                newKey = A[infoList[2]] + shortest[v]
                                oldKey = heap.entry_finder[v][0]
                                key = min(newKey, oldKey)
                        else:
                                key = A[infoList[2]] + shortest[v]

                        heap.add_task(v, key)

        print(A[7],A[37],A[59],A[82],A[99],A[115],A[133],A[165],A[188],A[197], sep=",")

filename = input("Filename:")
Graph = graph()

Graph.loadGraph(filename)

dijkstra(Graph)