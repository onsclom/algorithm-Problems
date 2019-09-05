import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original = list(nums)
        self.new = list(nums)

    def reset(self) -> List[int]:
        self.new=list(self.original)
        return list(self.new)
        

    def shuffle(self) -> List[int]:
        random.shuffle(self.new)
        return list(self.new)