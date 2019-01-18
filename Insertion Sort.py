def insertionSort(arr):
    for i in range(1,len(arr)):
        currentVal = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j] > currentVal:
                arr[j+1] = arr[j]
                arr[j] = currentVal
    return arr

print(insertionSort([5,9,1,3,0]))