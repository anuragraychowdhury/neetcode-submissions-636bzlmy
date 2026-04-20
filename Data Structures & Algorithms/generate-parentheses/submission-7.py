class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open_paren, close_paren, subset):
            if open_paren == close_paren == 0:
                res.append("".join(subset))
                return 
            
            if open_paren > 0:
                subset.append('(')
                dfs(open_paren - 1, close_paren, subset)
                subset.pop()
            
            if close_paren > open_paren:
                subset.append(')')
                dfs(open_paren, close_paren - 1, subset)
                subset.pop()

            
        dfs(n,n,[])
        return res
