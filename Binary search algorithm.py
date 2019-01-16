#Assume sorted array only
def binarySearch(arr, value):
    left = min(range(len(arr))) #left pointer
    right = max(range(len(arr))) #right pointer
    while left < right:
        middle = round((right+left)/2)
        if arr[middle] == value:
            return middle
        elif arr[middle] > value:
            right = middle
        elif arr[middle] < value:
            left = middle
    return -1

print(binarySearch([2,5,6,9,13,15,28],15)) #example input