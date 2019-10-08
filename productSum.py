def productSum(array, mult=1):
	runningSum=0
	for x in array:
		if (type(x)==int):
			runningSum += mult*x
		else:
			runningSum += mult*productSum(x, mult+1)
	return runningSum
