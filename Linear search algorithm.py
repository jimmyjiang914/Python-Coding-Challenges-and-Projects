def linearSearch(array, value):
    counter = 0
    for i in range(len(array)):
        if array[i] == value:
            return i
            break
        else:
            counter += 1
            continue
    if counter == len(array):
        return -1

print(linearSearch([100],200)) #Example input
