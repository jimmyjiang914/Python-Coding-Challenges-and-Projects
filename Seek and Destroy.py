def destroyer(arr):

    arr_target = arr[0]
    arr_constraint = arr[1:]
    arr_target = [index for index in arr_target if index not in arr_constraint]
    arr = arr_target

    return arr



print(destroyer((["tree", "hamburger", 53], "tree", 53)))