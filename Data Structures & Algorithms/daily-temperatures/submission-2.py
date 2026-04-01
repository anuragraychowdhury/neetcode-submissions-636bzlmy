class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n

        for r in range(n):
            while stack and temperatures[r] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = r - prev_index
            stack.append(r)
        return res