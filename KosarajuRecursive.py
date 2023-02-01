# Implements Kosaraju's algorithm with recursion
# Times out on larger inputs

import sys

sys.setrecursionlimit(875715)

def createAdjacencyList(edgeList) -> dict:
    vertex = 0
    vertexList = []
    adjacencyList = {}
    for edge in edgeList:
        if edge[0] != vertex:
            if vertex != 0:
                adjacencyList[vertex] = vertexList
            vertex = edge[0]
            vertexList = []
            if edge[1] != vertex:
                vertexList.append(edge[1])
        else:
            if edge[1]!= vertex:
                vertexList.append(edge[1])
    adjacencyList[vertex] = vertexList
    return adjacencyList

with open('SCC.txt') as f:
    edgeList = [[int(x) for x in l.strip().split(' ')] for l in f]

adjacencyList = createAdjacencyList(edgeList)

def reverseAdjacencyList(adjacencyList) -> dict:
    reverseAdjacencyList = {}
    for key, value in adjacencyList.items():
        for i in value:
            if not(i in reverseAdjacencyList):
                reverseAdjacencyList[i] = []
            reverseAdjacencyList[i].append(key)
    return reverseAdjacencyList

listOfFlags = {}
#finishingTime = 0
leaderVertex = None
listOfFinishingTimes = []
listOfStronglyConnectedComponents = {}

def depthFirstSearchLoop(adjacencyList, listOfFlags, processingOrder, inFirstPass):
    #print(processingOrder)
    for vertexNumber in processingOrder:
        if not(vertexNumber in listOfFlags.keys()):
            global leaderVertex
            leaderVertex = vertexNumber
            #print(f'> {vertexNumber}')
            depthFirstSearch(adjacencyList, vertexNumber, inFirstPass)

def depthFirstSearch(adjacencyList, startVertex, inFirstPass):
    stack = [(startVertex, 0)]
    global listOfFinishingTimes
    global leaderVertex
    while stack:
        vertex, st = stack[-1]
        stack.pop()
        stack.append((vertex, st + 1))
        #print('vertex: ' + str(vertex) + ', st:' + str(st))
        #print(f'dfs {startVertex}')
        if st == 0:
            listOfFlags[vertex] = 0
        if vertex in adjacencyList:
            if len(adjacencyList[vertex]) > st:
                edge = adjacencyList[vertex][st]
                if not(edge in listOfFlags):
                    stack.append((edge, 0))
                continue
        if inFirstPass == True:
            listOfFinishingTimes.append(vertex)
        elif inFirstPass == False:
            if leaderVertex not in listOfStronglyConnectedComponents:
                listOfStronglyConnectedComponents[leaderVertex] = []
            listOfStronglyConnectedComponents[leaderVertex].append(vertex)
        stack.pop()
            #print(leneaderVertex, startVertex)

def findStronglyConnectedComponents(adjacencyList):
    global listOfFlags
    global leaderVertex
    global listOfStronglyConnectedComponents
    reversedAdjacencyList= reverseAdjacencyList(adjacencyList)
    reverseProcessingOrder = list(reversed(sorted(reversedAdjacencyList.keys())))
    #print(reverseProcessingOrder)
    #print(reversedAdjacencyList)
    depthFirstSearchLoop(reversedAdjacencyList, listOfFlags, reverseProcessingOrder, True)
    leaderVertex = None
    listOfFlags = {}
    depthFirstSearchLoop(adjacencyList, listOfFlags, listOfFinishingTimes[::-1], False)
    #print(listOfFinishingTimes[::-1])
    listOfLengthOfStronglyConnectedComponents = []
    for key, value in listOfStronglyConnectedComponents.items():
        listOfLengthOfStronglyConnectedComponents.append(len(value))
    return listOfLengthOfStronglyConnectedComponents

print(sorted(findStronglyConnectedComponents(adjacencyList))[-5:])