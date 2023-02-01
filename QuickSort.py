# Quicksort with options for both 2 way and 3 way partitioning

import random
import math

def PartitionAroundPivot3(D, l , r):

    b = int(math.ceil((r - l + 1) / 2)) - 1 + l

    if D[l] < D[b]:
        if D[b] < D[r]:
            index = b
        elif D[l] < D[r]:
            index = r
        else:
            index = l
    else:
        if D[l] < D[r]:
            index = l
        elif D[b] < D[r]:
            index = r
        else:
            index = b

    temp = D[index]
    D[index] = D[l]
    D[l] = temp

    i = l + 1
    for j in range(l + 1, r + 1):
        if D[j] < D[l]:
            temp = D[i]
            D[i] = D[j]
            D[j] = temp
            i += 1

        j += 1

    temp = D[l]
    D[l] = D[i - 1]
    D[i - 1] = temp

    return i - 1

def PartitionAroundPivot1(D, l , r):

    i = l + 1
    for j in range(l + 1, r + 1):
        if D[j] < D[l]:
            temp = D[i]
            D[i] = D[j]
            D[j] = temp
            i += 1

        j += 1

    temp = D[l]
    D[l] = D[i - 1]
    D[i - 1] = temp

    return i - 1

def PartitionAroundPivot2(D, l , r):

    index = r

    temp = D[index]
    D[index] = D[l]
    D[l] = temp

    i = l + 1
    for j in range(l + 1, r + 1):
        if D[j] < D[l]:
            temp = D[i]
            D[i] = D[j]
            D[j] = temp
            i += 1

        j += 1

    temp = D[l]
    D[l] = D[i - 1]
    D[i - 1] = temp

    return i - 1

def QuickSort(A, l, r):

    if r - l + 1 == 1:
        return 0
    if r - l + 1 <= 0:
        return 0

    y = PartitionAroundPivot3(A, l , r)

    z1 = QuickSort(A, l, y - 1)
    z2 = QuickSort(A, y + 1, r)

    return  r - l + z1 +z2

numbers = []
filename = input("Filename:")
with open(filename) as f:
    lines = f.readlines()

f.close

count = 0
for line in lines:
    numbers.append(int(line))
    count += 1

Comparisons = QuickSort(numbers, 0 , count - 1)

print(Comparisons)