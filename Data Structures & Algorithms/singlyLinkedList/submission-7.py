class ListNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.dummy = ListNode(float('inf'), None)
        self.size = 0
    
    def get(self, index: int) -> int:
        count = 0
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.dummy.next
        
        while count < index:
            curr = curr.next
            count += 1
        return curr.value

    def insertHead(self, val: int) -> None:
        node = ListNode(val, self.dummy.next)
        self.dummy.next = node
        self.size += 1

    def insertTail(self, val: int) -> None:
        curr = self.dummy
        while curr.next:
            curr = curr.next
        node = ListNode(val, None)
        curr.next = node
        self.size += 1
        return

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        
        curr = self.dummy
        count = 0

        while curr and curr.next:
            if count == index:
                break
            curr = curr.next
            count += 1

        curr.next = curr.next.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.dummy.next

        while curr:
            res.append(curr.value)
            curr = curr.next
        return res
        
