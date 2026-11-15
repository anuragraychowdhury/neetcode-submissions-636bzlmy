class Solution:
    def climbStairs(self, n: int) -> int:
        ways_zero = 1
        ways_one = 1
        
        if n <= 1:
            return ways_zero
        
        for _ in range(n - 1):
            res = ways_zero + ways_one
            ways_zero = ways_one
            ways_one = res
        return res


