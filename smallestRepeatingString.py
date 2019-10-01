import sys
import math

def sublist(s, x) -> list:
    answer=[]
    for n in range(x):
        answer.append(s[n])
    return answer
        
def reverse(s):
    for x in range(1,len(s),1):
        test = sublist(s, x)
        good = True

        for y in range(1,len(s),1):
            cur = len(test)
            index=y%cur
            if (s[y]!=test[index]):
                good = False
            
        if good==True:
            return test
        
    return []

s = input()
s = list(s)
        
    
print("".join(reverse(s)))