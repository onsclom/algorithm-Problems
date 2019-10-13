def hasSingleCycle(array):
    seen = set()
	
	cur = 0
	
	while cur not in seen:
		seen.add(cur)
		cur = (cur+array[cur])%len(array)
		
	if len(seen) == len(array) and cur == 0:
		return True

	return False