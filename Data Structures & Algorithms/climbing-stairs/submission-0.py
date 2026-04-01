class Solution:
    def climbStairs(self, n: int) -> int:
        def recurse(i):
            if i == 1:
                return 1
            elif i == 2:
                return 2
            else:
                return recurse(i - 1) + recurse(i - 2)
        return recurse(n)
            

