def bubblesort(arr):
    for i in range(len(arr),1, -1):
        swaps = 0
        for j in range(0,i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                swaps += 1
        if swaps == 0:
            return arr
    return arr

print(bubblesort([46,53,86,4,2]))
