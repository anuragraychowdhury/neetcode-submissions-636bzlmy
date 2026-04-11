class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def dfs(index, curr_xor):
            nonlocal total
            if index == len(nums):
                total += curr_xor
                return
            dfs(index + 1, curr_xor = curr_xor ^ nums[index])
            dfs(index + 1, curr_xor)
        dfs(0, 0)
        return total
