class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = [0]
        def dfs(index, xor_sum):
            if index == len(nums):
                total[0] += xor_sum
                return
            dfs(index + 1, xor_sum ^ nums[index])
            dfs(index + 1, xor_sum)


        dfs(0,0)
        return total[0]