def whatIsInAName(collection, source):
    arr = []
    keys = source.keys()
    for dictionary in collection:
        length_check = 0
        for key in keys:
            if key in dictionary:
                if source[key] == dictionary[key]:
                    length_check = length_check + 1
            else:
                continue
        if length_check == len(keys):
            arr.append(dictionary)
    return arr

print(whatIsInAName([{ "first": "Romeo", "last": "Montague" }, { "first": "Mercutio", "last": "null" }, { "first": "Tybalt", "last": "Capulet" }], { "last": "Capulet" }))

