class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def partition_palindrome(partition_index, subset):
            if partition_index == len(s):
                res.append(subset.copy())
                return
            
            for i in range(partition_index, len(s)):
                curr_str = s[partition_index:i+1]
                if curr_str == curr_str[::-1]:
                    subset.append(curr_str)
                    partition_palindrome(i+1, subset)
                    subset.pop()
        
        partition_palindrome(0, [])
        return res