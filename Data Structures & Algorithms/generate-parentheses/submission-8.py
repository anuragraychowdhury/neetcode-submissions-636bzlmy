class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def parenthesis(openCount, closeCount, subset):
            if openCount == closeCount == 0:
                res.append("".join(subset.copy()))
                return
            
            if openCount > 0:
                subset.append("(")
                parenthesis(openCount - 1, closeCount, subset)
                subset.pop()
            
            if closeCount > openCount:
                subset.append(")")
                parenthesis(openCount, closeCount - 1, subset)
                subset.pop()
            
            return
        
        parenthesis(n,n,[])
        return res
        
