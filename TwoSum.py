#Finds two elements that sum to a particular integer if they exist in the input array

file = input("Filename:")
with open(file) as f:
    lines = f.readlines()
f.close()

lines = list(map(int, lines))
lines.sort()

dictSum = { 0: False }

#keep track of whether this sum has been seen before
for i in range(1,10001):
    dictSum[i] = False
    dictSum[-i] = False

# initialise 2 pointers, one from the end and one from the start
x = 0
y = len(lines) - 1
Count = 0

while x < y:
    #increase x if the sum is lower than -10000.
    #if this if statement is chosen before we have changed x or y at all, we eliminate all elements too small to form a sum in range even when added to the largest element
    # else we eliminate all elements too small for a sum when added to the largest element in our selection
    if lines[x] + lines[y] < -10000:
        x += 1
    # decrease y if it is larger than 10000.
    #if this is chosen first instead, we eliminate all elements too large to have potential to be part of a sum
    # else we eliminate all elements too large for a sum when added to the smallest element in our selection
    elif lines[x] + lines[y] > 10000:
        y -= 1
    else:
        # this is the step at which you have an in range array. The first + last elements have a sum in range, and the first element added to any other element can therefore only have a sum less than 10000
        # we therefore iterate from the last to first element, checking the sum of every element added to the first one
        for i in range(y , x, -1):
            # break if the sum goes out of range and return to the main while loop after incrementing x outside this loop
            if lines[x] + lines[i] < -10000:
                break
            # make sure the two elements are distinct, duplicates are possible
            if lines[x] != lines[i]:
                # mark the sum as seen and increment the count
                if dictSum[lines[x] + lines[i]] == False:
                    Count += 1
                    dictSum[lines[x] + lines[i]] = True
        x += 1

print(Count)

#this works because we find all the sums for a particular element x that has the potential to be part of a sum in the range.
# we need not check elements smaller the ones we have selected, as those are too small to form a sum even when added to the largest potential element in lines
# we need not check elements larger than the ones we have selected as those are too large to form a sum even when added to the smallest potential element in lines