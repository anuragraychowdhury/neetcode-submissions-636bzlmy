class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        mono_stack = []

        for curr_ind, curr_temp in enumerate(temperatures):
            while mono_stack and mono_stack[-1][0] < curr_temp:
                popped_temp, popped_ind = mono_stack.pop()
                res[popped_ind] = curr_ind - popped_ind
            mono_stack.append((curr_temp, curr_ind))
        return res