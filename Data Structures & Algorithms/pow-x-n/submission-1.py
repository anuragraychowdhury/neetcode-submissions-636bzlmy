class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        else:
            temp = 1
            for i in range(abs(n)):
                temp *= x
            
            if n > 0:
                return temp
            else:
                return 1/temp

            





