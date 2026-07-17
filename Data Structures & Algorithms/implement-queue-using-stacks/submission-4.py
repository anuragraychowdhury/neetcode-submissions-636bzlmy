class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if self.push_stack and not self.pop_stack:
            for i in range(len(self.push_stack)):
                self.pop_stack.append(self.push_stack.pop())
        
        elem = self.pop_stack.pop()
        return elem

    def peek(self) -> int:
        if self.pop_stack:
            return self.pop_stack[-1]
        return self.push_stack[0]

    def empty(self) -> bool:
        return (len(self.push_stack) == 0 and len(self.pop_stack) == 0)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()