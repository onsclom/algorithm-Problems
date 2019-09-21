#https://leetcode.com/problems/number-of-enclaves/

class Solution:
    
    def numEnclaves(self, A: List[List[int]]) -> int:
        #Assume all islands are enclaves
        enclaveTracker = list(A)
        
        for y in range(len(A)):
            if y == 0 or y == len(A)-1:
                #iterate on whole row
                for x in range(len(A[0])):
                    if A[y][x] == 1:
                        self.enclaveEliminator(enclaveTracker, A, x, y)
            else:
                if A[y][0] == 1:
                    self.enclaveEliminator(enclaveTracker, A, 0, y)
                if A[y][len(A[0])-1] == 1:
                    self.enclaveEliminator(enclaveTracker, A, len(A[0])-1, y)
                   
        res = 0        
        for y in range(len(A)):
            for x in range(len(A[0])):
                if enclaveTracker[y][x] == 1 and A[y][x] == 1:
                    res += 1
                    print("x then y")
                    print(x)
                    print(y)
                    
        return res
            
    def enclaveEliminator(self, tracker, islands, x, y):
        neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
        stack = []
        
        tracker[y][x] = 0
        stack.append([y, x])
        
        while(len(stack)!=0):
            current = stack.pop(0)
            cury, curx = current[0], current[1]
            
            for i in neighbors:
                if curx+i[0] >= 0:
                    if curx+i[0] < len(islands[0]):
                        if cury+i[1] >= 0 and cury+i[1] < len(islands):
                            if islands[cury+i[1]][curx+i[0]] == 1 and tracker[cury+i[1]][curx+i[0]] == 1:
                                tracker[cury+i[1]][curx+i[0]] = 0
                                stack.append([cury+i[1], curx+i[0]])
        