class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def dfs(partition_index, subset):
            if partition_index == len(s):
                res.append(subset.copy())
                return

            for i in range(partition_index, len(s)):
                curr = s[partition_index:i+1]
                if curr == curr[::-1]:
                    subset.append(curr)
                    dfs(i + 1, subset)
                    subset.pop()
        
        dfs(0,[])
        return res