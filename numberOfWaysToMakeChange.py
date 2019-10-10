def numberOfWaysToMakeChange(n, denoms):
	ways = [0 for x in range(n+1)]
	ways[0] = 1
	
	for x in denoms:
		for y in range(n+1):
			if y-x>=0:
				ways[y] += ways[y-x]
	
	return ways[n]
