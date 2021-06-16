arraySize = int(input("Enter the array size:"))

def hashIndex(key, arraySize):
    return key % arraySize

array = [None] * arraySize

def insert(array, key, arraySize):
    if array[hashIndex(key, arraySize)] == None:
        array[hashIndex(key, arraySize)] = key
    else:
        for n in range(len(array)):
            if (hashIndex(key, arraySize))+n >= len(array):
                n = n - len(array)
            if array[hashIndex(key, arraySize)+n] == None:
                array[hashIndex(key, arraySize)+n] = key
                break

def delete(array, key, arraySize):
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
print(array)
delete(array,8,arraySize)
print(array)
