class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        yo = set()

        for num in nums:
            if num in yo:
                return True
            else:
                yo.add(num)
        return False