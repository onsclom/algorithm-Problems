# 4sum_ii  on leetcode
# https://leetcode.com/problems/4sum-ii/
from typing import *

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        
        myDict = {}
        amount = 0
        
        for i in A:
            for j in B:
                if (i+j) in myDict:
                    myDict[i+j] += 1
                else:
                    myDict[i+j] = 1
                    
        for i in C:
            for j in D:
                if -1*(i+j) in myDict:
                    amount += myDict[-1*(i+j)]
                    
        return amount
        