class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for elem in operations:
            if len(stack) >= 2 and elem == '+':
                stack.append(stack[-1] + stack[-2])
            elif len(stack) >= 1 and elem == 'C':
                stack.pop()
            elif len(stack) >= 1 and elem == 'D':
                stack.append(2*stack[-1])
            else:
                stack.append(int(elem))
        return sum(stack)