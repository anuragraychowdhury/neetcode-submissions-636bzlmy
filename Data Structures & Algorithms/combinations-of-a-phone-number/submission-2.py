class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        
        res = []
        def dfs(index, subset):
            if len(subset) == len(digits):
                res.append("".join(subset))
                return 
            
            curr_digit = digits[index]
            codes = mapping[curr_digit]
            for i in range(len(codes)):
                subset.append(codes[i])
                dfs(index + 1, subset)
                subset.pop()
        
        if not digits:
            return res
        
        dfs(0,[])
        return res