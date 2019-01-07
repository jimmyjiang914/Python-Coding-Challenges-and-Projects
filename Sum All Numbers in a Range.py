def sumAll(arr):
    if arr[0] < arr[1]:
        full_arr = range(arr[0],arr[1]+1,1)
    elif arr[0] > arr[1]:
            full_arr = range(arr[1],arr[0]+1,1)
    else:
        full_arr = arr
    return(sum(full_arr))
    
