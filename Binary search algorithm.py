#Assume sorted array only
def binarySearch(arr, value):
    import math
    left = min(range(len(arr))) #left pointer
    right = max(range(len(arr))) #right pointer
    while left <= right:
        middle = math.floor((right + left) / 2)
        if arr[middle] == value:
            return middle
        elif arr[middle] > value:
            right = middle - 1
        elif arr[middle] < value:
            left = middle + 1
    return -1

print(binarySearch([2,5,6,9,13,15,28,30],3)) #example input