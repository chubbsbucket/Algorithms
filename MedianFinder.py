# returns the sum of all medians of a stream of numbers
import heapq
class Heap:
        def __init__ (self):
                self.heap = []
                self.size = 0

        def addKey(self, key):
               heapq.heappush(self.heap, key)
               self.size += 1

        def popKey(self, Bool):
            if Bool == False:
                x = heapq.heappop(self.heap)
                self.size -= 1
            elif Bool == True:
                x = heapq.heappop(self.heap)
                heapq.heappush(self.heap, x)
            return x


file = input("Filename:")

with open(file) as f:
    lines = f.readlines()

f.close()

# heap containing the larger half of elements and supporting extract min
maxHeap = Heap()

# heap containing smaller half of elements and supporting extract max
minHeap = Heap()

lineCount = 0
medians = []
for line in lines:

    # number of integers added
    lineCount += 1

    if lineCount > 1 and int(line) > medians[lineCount - 2]:
        maxHeap.addKey(int(line))

    if lineCount > 1 and int(line) < medians[lineCount - 2]:
        minHeap.addKey(-int(line))
    # start by adding to the maxHeap, you could do it with the min heap too
    elif lineCount == 1:
        maxHeap.addKey(int(line))

    # the min heap is allowed at most half the integers added or the bottom half excluding the median for odd lineCount
    while minHeap.size > lineCount // 2:
        key = minHeap.popKey(False)
        maxHeap.addKey(-key)
    # the max heap is allowed at most half the elements + 1 for even lineCount or upper half + median for odd lineCount
    while maxHeap.size > lineCount // 2 + 1:
        key = maxHeap.popKey(False)
        minHeap.addKey(-key)

    # if lineCount is even
    if lineCount % 2 == 0:
        # if your minheap has half the elements, it has the i/2th smallest element which is the median. this element is also the largest element in the min heap, and is removed by extract max
        if minHeap.size == lineCount // 2:
            median = minHeap.popKey(True)
            medians.append(-median)
        # else it has less than half the elements i.e. it has i // 2 - 1, and the max heap has i // 2 + 1, as the max heap can't take any more than that.
        else:
            # pop the smallest from the max heap, which would be the i/2 th smallest element, the median
            median = maxHeap.popKey(True)
            medians.append(median)
    # if lineCount is odd, your max heap must have lineCount// 2 + 1 elements because your minHeap can only have lineCount // 2 elements, and your total number of elements is lineCount//2 * 2 + 1
    # since minHeap can only have <= than lineCount // 2, and maxHeap <= lineCount//2 + 1 you end up with lineCount//2 + 1 in the maxHeap every time
    else:
        # smallest element in maxheap gives your median
        median = maxHeap.popKey(True)
        medians.append(median)


medianSum = 0
for median in medians:
    medianSum += median

print(medianSum % 10000)