class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(index, subset):
            if index == len(nums):
                res.append(subset.copy())
                return 
            
            subset.append(nums[index])
            dfs(index + 1, subset)
            subset.pop()
            
            # call where you include the next number
            dfs(index + 1, subset)
        
        dfs(0, [])
        return res


