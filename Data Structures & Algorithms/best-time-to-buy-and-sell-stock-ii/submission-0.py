class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            current_price = prices[i]
            next_price = prices[i+1]

            if next_price - current_price > 0:
                profit += next_price - current_price
        return profit