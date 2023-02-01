#uses mergesort to count the inversions in an array
def MergeAndCountSplitInv(B, C , n, len1, len2):
    D = []
    i = 0
    j = 0
    z = 0
    for k in range(0, n):
        while i < len1 and j < len2:
            if B[i] <= C[j]:
                D.append(B[i])
                i += 1
            else:
                D.append(C[j])
                j += 1
                z += (len1 - i)
            k += 1

        while j < len2 and i >= len1:
                D.append(C[j])
                k += 1
                j += 1

        while i < len1 and j >= len2:
                D.append(B[i])
                k += 1
                i += 1

    return (D, z)


def SortAndCount(A, n):

    if n == 1:
        return (A, 0)

    middle = n // 2
    length1 = n // 2
    length2 = n - (n // 2)

    (B, x) = SortAndCount(A[:middle], length1)
    (C, y) = SortAndCount(A[middle:], length2)

    (D, z) = MergeAndCountSplitInv(B, C, n, length1, length2)

    return (D, x + y + z)


numbers = []
filename = input("Filename:")
with open(filename) as f:
    lines = f.readlines()

f.close

count = 0
for line in lines:
    numbers.append(int(line))
    count += 1

(SortedArr, inversions) = SortAndCount(numbers, count)

print(inversions)