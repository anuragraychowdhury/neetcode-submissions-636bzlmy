class Solution:
    def climbStairs(self, n: int) -> int:
        # [0,0,0]
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        if n <= 1:
            return dp[n]
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        