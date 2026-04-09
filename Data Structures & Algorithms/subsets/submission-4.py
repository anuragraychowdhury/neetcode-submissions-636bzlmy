class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(index, subset):
            if index == len(nums):
                res.append(subset.copy())
                return 
            
            # call where you don't include the next number
            dfs(index + 1, subset)
            
            # call where you include the next number
            subset.append(nums[index])
            dfs(index + 1, subset)
            subset.pop()
        
        dfs(0, [])
        return res


