class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for elem in s:
            if elem in closeToOpen:
                if stack and stack[-1] == closeToOpen[elem]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(elem)
        return True if len(stack) == 0 else False