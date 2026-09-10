class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0 and a < 0:
                    if abs(a) == stack[-1]:
                        a = 0
                        stack.pop()
                    elif abs(a) < stack[-1]:
                        a = 0
                    else:
                        stack.pop()
            
                if a != 0:
                    stack.append(a)
        return stack