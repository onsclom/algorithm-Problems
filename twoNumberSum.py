def twoNumberSum(array, targetSum):
    numSet = set()
	for x in array:
		if (targetSum - x) in numSet: #then there is a match
			if x <= targetSum-x:
				return [x, targetSum-x]
			else:
				return [targetSum-x, x]
		if x not in numSet:
			numSet.add(x)
	return []