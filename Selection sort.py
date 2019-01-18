def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min = j
        if i != min:
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp
    return arr

print(selectionSort([53,67,3,7,8,1]))


