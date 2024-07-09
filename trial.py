import matplotlib.pyplot as plt
import time
import random

# Algorithm 1: Linear Search
# Description: Given an unsorted array of integers and a target value, find the index of the first occurrence of the target value in the array. If the target value is not found, return -1.
def linear_search(arr, target):
    for i in range(0,len(arr)-1):
        if arr[i] == target:
            return i
    return -1

#analysis of runtime (input is list is length n with 1000<n<10000)
points = []
for i in range(1, 10000):
    arr = []
    for j in range(0,i):
        arr.append(random.randint(1,i*100))
    target = random.randint(1,i*100)
    start = time.time()
    k = linear_search(arr, target)
    end = time.time()
    if end-start != 0:
        points.append((i,end-start))
x, y = zip(*points)
plt.scatter(x, y)  # or plt.plot(x, y) for individual points
plt.title('Runtime for linear_search(arr, target)')
plt.xlabel('Length of List input, n')
plt.ylabel('Length of Runtime in Seconds')
plt.grid(True)
plt.show()