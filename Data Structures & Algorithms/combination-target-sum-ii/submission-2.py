class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        subset = []

        def dfs(index, curr_sum, subset):
            if curr_sum == target:
                result.append(subset.copy())
                return 
            if curr_sum > target or index >= len(candidates):
                return
            
            subset.append(candidates[index])
            dfs(index + 1, curr_sum + candidates[index], subset)
            subset.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            dfs(index + 1, curr_sum, subset)
        
        dfs(0,0,subset)
        return result

