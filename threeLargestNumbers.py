def findThreeLargestNumbers(array):
    largest=None
	secondLargest=None
	thirdLargest=None
	
	for x in array:
		if largest==None or x>largest:
			thirdLargest = secondLargest
			secondLargest = largest
			largest = x
		elif secondLargest==None or x>secondLargest:
			thirdLargest = secondLargest
			secondLargest = x
		elif thirdLargest==None or x>thirdLargest:
			thirdLargest = x
	
	return [thirdLargest, secondLargest, largest]