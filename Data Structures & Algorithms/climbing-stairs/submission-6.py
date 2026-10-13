class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        second = 2
        first = 1

        for i in range(3, n + 1):
            res = first + second
            first = second
            second = res
        
        return res
