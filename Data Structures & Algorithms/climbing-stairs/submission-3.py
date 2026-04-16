class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 2
        if n == 1:
            return first
        elif n == 2:
            return second
        
        for i in range(3,n+1):
            third = first + second
            first = second
            second = third
        return third
        
        