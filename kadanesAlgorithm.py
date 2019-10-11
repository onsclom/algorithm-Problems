def kadanesAlgorithm(array):
    curMax = array[0]
    runningSum = 0
    for x in array:
        if runningSum + x > 0:
                runningSum += x
                if runningSum > curMax:
                    curMax = runningSum
        else:
			#cannot return empty array sum = 0
            if runningSum + x > curMax: 
                curMax = runningSum + x
            runningSum = 0
    return curMax

			