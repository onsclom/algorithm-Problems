def selectionSort(array):
    for x in range(len(array)):
        min = x
        for y in range(x, len(array), 1):
            if array[y]<array[min]:
                min = y
        array[x],array[min] = array[min],array[x]
    return array