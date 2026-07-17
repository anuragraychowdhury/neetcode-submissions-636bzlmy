class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_map = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if stack and paren_map[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0