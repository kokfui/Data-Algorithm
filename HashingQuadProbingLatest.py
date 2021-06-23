arraySize = int(input("Enter the array size:"))

def hashIndex(key, arraySize):
    return key % arraySize

array = [None] * arraySize

def insert(array, key, arraySize):
    if array[hashIndex(key, arraySize)] == None:
        array[hashIndex(key, arraySize)] = key
    else:
        for n in range(len(array)):
            quad=(n+1)^2
            if (hashIndex(key, arraySize))+quad >= len(array):
                value = (hashIndex(key, arraySize) + quad) / len(array)
                y = (hashIndex(key, arraySize)+quad) - int(value*(len(array)))
                if array[y] == None:
                    array[y] = key
                    break
            if array[hashIndex(key, arraySize)+quad] == None:
                array[hashIndex(key, arraySize)+quad] = key
                break

def delete(array, key):
    for n in range(len(array)):
        if array[n] == key:
            array[n] = None

print(array)
insert(array, 5, arraySize)
insert(array, 6, arraySize)
insert(array, 11, arraySize)
insert(array, 12, arraySize)
insert(array, 3, arraySize)
insert(array, 16, arraySize)
insert(array, 17, arraySize)
insert(array, 8, arraySize)
print(array)
