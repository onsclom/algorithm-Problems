# Longest substring with at lask k repeating characters
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/submissions/

#O(n) solution! Very interesting
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return self.longestSubRecursive(s, k)
        
    def longestSubRecursive(self, s: str, k: int) -> int:
        if s == "":
            return 0
        
        dictionary = {}
        
        for x in s:
            if x in dictionary:
                dictionary[x]+=1
            else:
                dictionary[x]=1
        valid = True;
        for x in dictionary:
            if dictionary[x] < k:
                valid = False;
        
        if valid == True:
            return len(s)
        else:
            #recurse on all split strings and get max
            splitStringNums = []
            start = 0
            currentString = ""
            for x in s:
                if (dictionary[x] < k):
                    splitStringNums.append(self.longestSubRecursive(currentString, k))
                    currentString = ""
                else:
                    currentString+=x
            #doing again in the case the last letter is legal
            splitStringNums.append(self.longestSubRecursive(currentString, k))
            return max(splitStringNums)
            
                
            

class bruteForceSlowSolution:
    def longestSubstring(self, s: str, k: int) -> int:
        highest = 0
        
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                #there exists a substring from s[i] to s[j]
                #and we must check that there exists atleast k of every char
                currentTest = s[i:j+1] 
                dictionary = {}
                for x in currentTest:
                    if x in dictionary:
                        dictionary[x]+=1
                    else:
                        dictionary[x]=1
                #go through dictionary and make sure everything is 2 or greater
                valid = True
                for y in dictionary:
                    if dictionary[y] < k:
                        valid = False 
                if (len(currentTest) > highest) and valid==True:
                    highest = len(currentTest)
        return highest
                
                