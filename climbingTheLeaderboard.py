import math
import os
import random
import re
import sys

#returns the index of the numbers placement in logn time!
def modifiedBinarySearch(numToSearch,scores):
    start=0
    end=len(scores)-1
    while ( start<end ):
        midNum = (start+end)//2
        midTerm = scores[midNum]
        if (numToSearch == midTerm):
            return midNum
        elif (numToSearch > midTerm):
            end = midNum-1
        else:
            start = midNum+1
    #if greater than start, add 1 since it goes after start
    if scores[start] > numToSearch:
        return start+1
    else:
        return start

        
    
def climbingLeaderboard(scores, alice):
    scoreList = list(set(scores))
    scoreList.sort(reverse=True)
    answers = []
    
    for x in alice:        
        answers.append(modifiedBinarySearch(x,scoreList)+1)
        
    return answers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()