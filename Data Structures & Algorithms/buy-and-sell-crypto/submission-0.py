class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        res = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                currProf = prices[r] - prices[l]
                res = max(res, currProf)
            else:
                l = r
            r += 1
        return res

        