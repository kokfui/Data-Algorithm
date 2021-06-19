arraySize = int(input("Enter the array size:"))

def hashIndex(key, arraySize):
    return key % arraySize

array = [[] for _ in range(arraySize)]

def insert(array, key, arraySize):
    array[hashIndex(key, arraySize)].append(key)
    
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
print(array)

