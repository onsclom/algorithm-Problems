# Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/submissions/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[]
        
        for i in range(1, n+1):
            current = ""
            if i%3==0:
                current += "Fizz"
            if i%5==0:
                current += "Buzz"
            if current == "":
                current = i
            answer.append(str(current))
            
        return answer