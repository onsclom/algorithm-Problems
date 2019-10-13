from math import inf

def minNumberOfCoinsForChange(n, denoms):
	memo = [inf for x in range(n+1)]
	memo[0] = 0
	for coin in denoms:
		for x in range(len(memo)):
			if x-coin >= 0:
				if memo[x-coin]+1 < memo[x]:
					memo[x] = memo[x-coin]+1
	return -1 if memo[n] == inf else memo[n]
		
		
