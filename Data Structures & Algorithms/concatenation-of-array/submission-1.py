class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * (n * 2)
        for i in range(len(res)):
            index = i % len(nums)
            res[i] = nums[index]
        return res

