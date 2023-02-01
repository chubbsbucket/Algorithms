# schedules jobs in order of priority, using a greedy algorithm

import math 
class job:
    def __init__ (self):
        self.length = 0
        self.weigth = 0
        self.score = 0
    def compute(self):
        self.score = self.weight - self.length

def printjob(j):
        print(j.weight)
        print("/")
        print(j.length)

def compareJobs(j1, j2):
    if j1.score > j2.score:
        return 1
    elif j1.score < j2.score:
        return 2
    elif j1.weight > j2.weight:
        return 1
    else:
        return 2
        
def merge(arr1, arr2):
    
    p1 = 0;
    p2 = 0;
    p3 = 0;
    
    l1 = len(arr1)
    l2 = len(arr2)
    
    arr3 = [0] * (l1 + l2)
    
    while(p3 <= l1 + l2 - 1):
        if p1 >= l1:
            arr3[p3] = arr2[p2]
            p2 = p2 + 1
            p3 = p3 + 1
            continue
        
        if p2 >= l2:
            arr3[p3] = arr1[p1]
            p1 = p1 + 1
            p3 = p3 + 1
            continue
        
        if compareJobs(arr1[p1], arr2[p2]) == 1:
            arr3[p3] = arr1[p1]
            p1 = p1 + 1
            p3 = p3 + 1
            continue
        else:
            arr3[p3] = arr2[p2]
            p2 = p2 + 1
            p3 = p3 + 1
            continue
    
    return arr3
    
def mergeSort(arr):
    arrLen = len(arr)
    if (arrLen <= 1):
        return arr
    
    ind = math.floor(arrLen // 2)
    
    arr1 = arr[:ind]
    arr2 = arr[ind:]
    
    return merge(mergeSort(arr1), mergeSort(arr2));

def greedy(jobslist, jobNumber):
    
    for j in jobslist:
        j.compute()
    
    sortedJobs = mergeSort(jobslist);
    
    CompletionTimes = [0] * jobNumber
    
    CompletionTimes[0] = sortedJobs[0].length

    for i in range(1, jobNumber):
        CompletionTimes[i] = sortedJobs[i].length + CompletionTimes[i - 1]
        
    weightedSum = 0
    
    for i in range(0, jobNumber):
        weightedSum = weightedSum + sortedJobs[i].weight*CompletionTimes[i]
        
    return weightedSum

file = input("Filename:")

with open(file) as f:
    lines = f.readlines()
f.close()

numOfJobs = int(lines[0])
jobs = [0] * (numOfJobs)

job_ind = 0

for i in range(1, numOfJobs + 1):
    x = lines[i].split()
    jobs[job_ind] = job()
    jobs[job_ind].weight = int(x[0])
    jobs[job_ind].length = int(x[1])
    job_ind = job_ind + 1



print(greedy(jobs, numOfJobs))
