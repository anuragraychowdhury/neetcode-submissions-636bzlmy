class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def partition_check(part_index, subset):
            if part_index == len(s):
                res.append(subset.copy())
                return
            
            for i in range(part_index, len(s)):
                prefix = s[part_index:i+1]
                if prefix == prefix[::-1]:
                    subset.append(prefix)
                    partition_check(i+1,subset)
                    subset.pop()
            return
        
        partition_check(0,[])
        return res