def maxSubsetSumNoAdjacent(array):
    cur, prev = 0, 0
    for x in array:
        if cur >= prev+x:
        	prev = cur
        else:
            cur, prev = prev, cur
            cur+=x 
    return cur
