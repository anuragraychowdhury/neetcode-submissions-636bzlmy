'''
[1,2,3]

dp = [1,2]

1 step from 2, (3), 1 step from 3, DONE
[1,2,3,done]

2 steps from 2, DONE
[1,2,0,done]

pick the smaller result 

cost
[1,2,3]
dp
[1,2,0]
'''


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp = [0] * len(cost)
        # dp[0] = cost[0]
        # dp[1] = cost[1]
        # n = len(cost)

        # for i in range(2, len(cost)):
        #     dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        # return min(dp[n-1], dp[n-2])

        first_step = cost[0]
        sec_step = cost[1]

        if len(cost) == 2:
            return min(cost)

        for i in range(2, len(cost)):
            curr = min(first_step, sec_step) + cost[i]
            first_step = sec_step
            sec_step = curr
        
        return min(curr, first_step)





