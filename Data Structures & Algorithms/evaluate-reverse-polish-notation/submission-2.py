class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in '+-*/':
                elem1 = stack.pop()
                elem2 = stack.pop()
                if t == '+':
                    stack.append(elem1 + elem2)
                elif t == '-':
                    stack.append(elem2 - elem1)
                elif t == '*':
                    stack.append(elem1 * elem2)
                elif t == '/':
                    stack.append(int(elem2 / elem1))
            else:
                stack.append(int(t))
        return stack[-1]
