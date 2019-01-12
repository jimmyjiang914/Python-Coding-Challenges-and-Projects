def diffArray(arr1, arr2):

    newArr_intersect = set(arr1).intersection(set(arr2))
    newArr = ((set(arr1))|(set(arr2))) - newArr_intersect

    return newArr

print(diffArray(["andesite", "grass", "dirt", "pink wool", "dead shrub"],
                ["diorite", "andesite", "grass", "dirt", "dead shrub"]))

