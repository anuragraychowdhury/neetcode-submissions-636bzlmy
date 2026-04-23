class Solution:
    def tribonacci(self, n: int) -> int:
        # dp = [0] * (n+1)
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        
        # dp[0] = 0
        # dp[1] = 1
        # dp[2] = 1
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        # return dp[n]

        prev_index = 1
        prev_index_2 = 1
        prev_index_3 = 0

        res = 0
        for i in range(3, n+1):
            res = prev_index + prev_index_2 + prev_index_3
            prev_index_3 = prev_index_2
            prev_index_2 = prev_index
            prev_index = res

        return res