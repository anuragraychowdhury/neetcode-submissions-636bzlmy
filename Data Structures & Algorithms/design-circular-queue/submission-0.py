class ListNode:
    def __init__(self, value, prev=None,next=None):
        self.value = value
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.length = 0
        self.front = ListNode(float('inf'))
        self.rear = ListNode(float('inf'))
        self.front.next = self.rear
        self.rear.prev = self.front

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        prev_front = self.rear.prev
        new_node = ListNode(value)
        self.rear.prev = new_node
        new_node.next = self.rear
        prev_front.next = new_node
        new_node.prev = prev_front

        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        remove = self.front.next
        self.front.next = remove.next
        remove.next.prev = self.front

        self.length -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.next.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.prev.value

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()