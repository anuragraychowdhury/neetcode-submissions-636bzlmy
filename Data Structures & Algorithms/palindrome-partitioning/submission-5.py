class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def partition_checker(index, subset):
            if index == len(s):
                res.append(subset.copy())
                return
            
            for i in range(index, len(s)):
                current_string = s[index: i+1]
                if current_string == current_string[::-1]:
                    subset.append(current_string)
                    partition_checker(i+1, subset)
                    subset.pop()
        
        partition_checker(0, [])
        return res