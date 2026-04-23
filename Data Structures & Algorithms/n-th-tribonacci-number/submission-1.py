class Solution:
    def tribonacci(self, n: int) -> int:
        zero = 0
        one = 1
        two = 1
        if n == 0:
            return zero
        if n == 1 or n == 2:
            return one
        for i in range(3, n+1):
            res = zero + one + two
            zero = one
            one = two
            two = res
        return res