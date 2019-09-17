class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        dict = {}
        
        for x in nums1:
            if x in dict:
                dict[x]+=1
            else:
                dict[x]=1
        
        answer = []
        
        for x in nums2:
            if x in dict and dict[x]>0:
                answer.append(x)
                dict[x]-=1
            
        return answer