def levenshteinDistance(str1, str2):
	if len(str1)>len(str2):
		big, small = " "+str1, " "+str2
	else:
		small, big = " "+str1, " "+str2
	
	firstRow = [i for i in range(len(small))]
	secondRow = [None for i in range(len(small))]
	
	for y in range(1, len(big), 1):
		for x in range(len(small)):
			cur = min(getNeighbors(x,firstRow,secondRow))
			if big[y]!=small[x]:
				cur += 1
			secondRow[x] = cur
		firstRow = list(secondRow)
		
	return firstRow[len(firstRow)-1]

def getNeighbors(x, row1, row2):
	answer=[]
	if x>0:
		answer.append(row1[x-1])
		answer.append(row2[x-1])
	answer.append(row1[x])
	
	return answer