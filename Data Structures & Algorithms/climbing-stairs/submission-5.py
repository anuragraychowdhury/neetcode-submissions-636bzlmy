class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        # first = 1
        # second = 2
        # if n == 1:
        #     return first
        # elif n == 2:
        #     return second
        
        # for i in range(3,n+1):
        #     third = first + second
        #     first = second
        #     second = third
        # return third
        
        