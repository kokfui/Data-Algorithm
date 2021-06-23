arraySize = int(input("Enter the array size:"))
primeNum = int(input("Enter the prime number:"))

def hashIndex(key, arraySize):
    return key % arraySize

def hashIndex2(key, primeNum):
    return primeNum - (key % primeNum)

array = [None] * arraySize

def insert(array, key, arraySize):
    if array[hashIndex(key, arraySize)] == None:
        array[hashIndex(key, arraySize)] = key
    else:
        for n in range(100):
            x = n + 1
            if hashIndex(key, arraySize) + x * hashIndex2(key, primeNum) >= len(array):
                value = (hashIndex(key, arraySize) + x * hashIndex2(key, primeNum)) / len(array)
                y = (hashIndex(key, arraySize) + x * hashIndex2(key, primeNum)) - int(value*(len(array)))
                if array[y] == None:
                    array[y] = key
                    break
            elif hashIndex(key, arraySize) + x * hashIndex2(key, primeNum) < len(array):
                if array[hashIndex(key, arraySize) + x * hashIndex2(key, primeNum)] == None:
                    array[hashIndex(key, arraySize) + x * hashIndex2(key, primeNum)] = key
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
insert(array, 4, arraySize)
insert(array, 17, arraySize)
insert(array, 2, arraySize)
print(array)
delete(array,6)
print(array)



