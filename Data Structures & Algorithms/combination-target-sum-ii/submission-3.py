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
            
            subset.append(candidates[index])
            curr_sum += candidates[index]
            dfs(index + 1, subset, curr_sum)
            subset.pop()
            curr_sum -= candidates[index]

            while index < len(candidates) - 1 and candidates[index] == candidates[index + 1]:
                index += 1
            
            dfs(index + 1, subset, curr_sum)
        
        dfs(0, [], 0)
        return res

