def bubblesort(arr):
    for i in range(len(arr),1, -1):
        for j in range(0,i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp

    return arr

print(bubblesort([46,53,86,4,2]))
