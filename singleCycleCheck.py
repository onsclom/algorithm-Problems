def hasSingleCycle(array):
    numsVisited = 0
	
    cur = 0
	
    while numsVisited < len(array):
		
        if numsVisited > 0 and cur == 0:
            return False
		
        cur = (cur+array[cur])%len(array)
		
        numsVisited += 1
		
    if cur == 0:
    	return True

    return False