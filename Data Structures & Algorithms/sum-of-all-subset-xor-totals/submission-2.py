class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def dfs(start_index, curr_xor):
            nonlocal total
            total += curr_xor

            for i in range(start_index, len(nums)):
                dfs(i + 1, curr_xor = curr_xor ^ nums[i])
            
        dfs(0, 0)
        return total
