from collections import Counter

def getRotations(list1, list2):

    mostCommonNum = Counter(list(list1 + list2)).most_common(1)[0][0]
    for i in range(len(list1)):
        if list1[i]!=mostCommonNum and list2[i]!=mostCommonNum: return -1
    return min(len(list1)-Counter(list1)[mostCommonNum], len(list1)-Counter(list2)[mostCommonNum])

##############
##TEST CASES##
##############
print( getRotations( [0,1,1,0,1] ,  [1,3,5,1,0] ) )     # 2
print( getRotations( [1,1,1,0] ,    [0,0,0,1] ) )       # 1
print( getRotations( [0,1,2,1] ,    [0,0,0,1] ) )       #-1
print( getRotations( [0,1,2,0] ,    [1,0,0,1] ) )       # 2
