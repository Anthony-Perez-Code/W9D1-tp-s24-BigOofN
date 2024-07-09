# Algorithm 1: Linear Search
# Description: Given an unsorted array of integers and a target value, find the index of the first occurrence of the target value in the array. If the target value is not found, return -1.
def linear_search(arr, target):
    for i in range(0,len(arr)-1):
        if arr[i] == target:
            return i
    return -1

#sample test cases
array = [10,23,45,70,11,15]
target = 70
print(f"Index of {target}: {linear_search(array, target)}") #Output: 3)
target = 11
print(f"Index of {target}: {linear_search(array, target)}") #Output: 4)
target = 99
print(f"Index of {target}: {linear_search(array, target)}") #Output: -1)

#Algorithm 2: Bubble Sort
#Description: Given an unsorted array of integers, sort the array in ascending order using the bubble sort algorithm.

def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0,len(arr) - 1):
            temp1 = arr[j]
            temp2 = arr[j + 1]
            if temp1 > temp2:
                arr[j] = temp2
                arr[j + 1] = temp1
    return arr

#sample test cases
array = [64, 34, 25, 12, 22, 11, 90]
print(f"Sorted array: {bubble_sort(array)}") #Output: [11, 12, 22, 25, 34, 64, 90]
array = [5, 1, 4, 2, 8]
print(f"Sorted array: {bubble_sort(array)}") #Output: [1, 2, 4, 5, 8]