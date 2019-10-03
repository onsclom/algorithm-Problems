def insertionSort(array):
    for x in range(len(array)):
        for y in range(x, 0, -1):
            if array[y]<array[y-1]:
                array[y],array[y-1]=array[y-1],array[y]
    return array