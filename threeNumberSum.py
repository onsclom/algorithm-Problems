def threeNumberSum(array, targetSum):
    hashSet = set()
    for x in array:
        hashSet.add(x)
	
    hashAnswers=set()
    answers=[]

    for x in range(len(array)):
        for y in range(x+1,len(array),1):
                third = targetSum-array[x]-array[y]
                if third != array[x] and third != array[y] and third in hashSet:
                    current = [array[x],array[y],int(third)]
                    current.sort()
                    searchItem = tuple(current)
                    if searchItem not in hashAnswers:
                        hashAnswers.add(searchItem)
                        answers.append(current)
                        
    answers.sort()
	
    return answers