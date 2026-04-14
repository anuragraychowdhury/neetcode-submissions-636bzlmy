class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(index, subset, curr_sum):
            if curr_sum == target:
                res.append(subset.copy())
                return
            if index >= len(candidates) or curr_sum > target:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                dfs(i + 1, subset, curr_sum + candidates[i])
                subset.pop()
        
        dfs(0, [], 0)
        return res

