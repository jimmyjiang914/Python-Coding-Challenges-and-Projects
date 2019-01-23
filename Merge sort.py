import math

def merge(arr1,arr2):
    i = 0
    j = 0
    newArr = []
    while i <= (len(arr1)-1) and j <= (len(arr2)-1):
        if arr1[i] <= arr2[j]:
            newArr.extend([arr1[i]])
            i += 1
        elif arr1[i] > arr2[j]:
            newArr.extend([arr2[j]])
            j += 1
    if i == len(arr1):
        newArr.extend(arr2[j:])
    elif j == len(arr2):
        newArr.extend(arr1[i:])

    return newArr

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    half = math.floor(len(arr)/2)
    left = mergeSort(arr[slice(0,half)])
    right = mergeSort(arr[slice(half,len(arr))])
    return merge(left,right)


print(mergeSort([10,24,76,73,72,1,9]))