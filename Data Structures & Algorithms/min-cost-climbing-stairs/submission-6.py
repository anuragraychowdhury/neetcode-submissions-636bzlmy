class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        '''
            cost = [10,15,20]
            dp = [10,15,0,0]
        '''
        
        n = len(cost)
        dp = [0] * (n)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return min(dp[n - 1], dp[n - 2])
