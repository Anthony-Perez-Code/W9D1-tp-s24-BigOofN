import matplotlib.pyplot as plt
import time
import random

def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0,len(arr) - 1):
            temp1 = arr[j]
            temp2 = arr[j + 1]
            if temp1 > temp2:
                arr[j] = temp2
                arr[j + 1] = temp1
    return arr

points = []
for i in range(1, 2000):
    arr = []
    for j in range(0,i):
        arr.append(random.randint(1,i*100))
    start = time.time()
    k = bubble_sort(arr)
    end = time.time()
    points.append((i,end-start))
    print(i)
x, y = zip(*points)
plt.scatter(x, y)  # or plt.plot(x, y) for individual points
plt.title('Runtime for linear_search(arr, target)')
plt.xlabel('Length of List input, n')
plt.ylabel('Length of Runtime in Seconds')
plt.grid(True)
plt.show()