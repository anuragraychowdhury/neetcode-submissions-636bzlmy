class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n >= 1:
            temp = 1
            for i in range(n):
                temp *= x
            return temp
        else:
            temp = 1
            for i in range(abs(n)):
                temp *= x
            return 1/temp

            





