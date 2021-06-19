arraySize = int(input("Enter the array size:"))

def hashIndex(key, arraySize):
    return key % arraySize

array = [None] * arraySize

def insert(array, key, arraySize):
    if array[hashIndex(key, arraySize)] == None:
        array[hashIndex(key, arraySize)] = key
    else:
        for n in range(len(array)):
            quad=n^2
            if (hashIndex(key, arraySize))+quad >= 2*(len(array)):
                quad = quad - 2*(len(array))
                if array[quad] == None:
                    array[quad] = key
                    break
            if (hashIndex(key, arraySize))+quad >= len(array):
                quad = quad - len(array)
                if array[quad] == None:
                    array[quad] = key
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
