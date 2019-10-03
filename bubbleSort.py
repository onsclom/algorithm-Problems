def bubbleSort(array):
	for x in range(len(array)-1):
		for y in range(0, len(array)-1-x, 1):
			if array[y] > array[y+1]:
				array[y], array[y+1] = array[y+1], array[y]
	return array
