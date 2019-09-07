class Solution:

    def __init__(self, nums: List[int]):
        self.original = list(nums)
        self.current = nums

    def reset(self) -> List[int]:
        self.new = list(self.original)
        return list(self.new)

    def shuffle(self) -> List[int]:
        for x in range(len(self.current)):
            randIndex = random.randrange(0, len(self.current))
            self.current[x], self.current[randIndex] = self.current[randIndex], self.current[x]
        return list(self.current)