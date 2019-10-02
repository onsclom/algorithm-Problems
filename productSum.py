#recursive
def productSumHelper(posArray, cur, rsum):
	if (type(posArray)==int):
		return cur*posArray
	csum = 0
	for x in posArray:
		csum+=productSumHelper(x, cur+1, rsum)
	return cur*csum

def productSum(array):
    runningSum=0
    for x in array:
        runningSum+=productSumHelper(x, 1, runningSum)
    return runningSum

#next to make one function version.. 

#then to make iterative version