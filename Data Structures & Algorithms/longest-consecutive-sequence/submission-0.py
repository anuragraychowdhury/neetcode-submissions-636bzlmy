class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            longest = 1
            while (num - longest) in nums:
                longest += 1
            res = max(res, longest)
        
        return res