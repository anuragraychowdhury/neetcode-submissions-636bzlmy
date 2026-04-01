class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.left = ListNode(float('inf'))
        self.right = ListNode(float('inf'))
        self.size = 0
        self.left.next = self.right
        self.right.prev = self.left

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        new_node = ListNode(value)

        prev_node = self.right.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = self.right
        self.right.prev = new_node

        self.size += 1

    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)

        next_to_left = self.left.next
        self.left.next = new_node
        next_to_left.prev = new_node
        new_node.next = next_to_left
        new_node.prev = self.left

        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        popped_node = self.right.prev
        pre_popped = popped_node.prev
        pre_popped.next = self.right
        self.right.prev = pre_popped
        self.size -= 1

        if self.size == 0:
            self.left.next = self.right
            self.right.prev = self.left


        return popped_node.val


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        popped_node = self.left.next
        post_popped = popped_node.next
        self.left.next = post_popped
        post_popped.prev = self.left
        self.size -= 1

        if self.size == 0:
            self.left.next = self.right
            self.right.prev = self.left

            
        return popped_node.val