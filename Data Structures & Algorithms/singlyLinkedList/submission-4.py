class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.dummy = ListNode(float('inf'))
        self.size = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.dummy.next
        ind = 0
        while curr:
            if ind == index:
                return curr.val
            curr = curr.next 
            ind += 1
        return -1           

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        curr = self.dummy
        nxt_node = curr.next 
        self.dummy.next = new_node
        new_node.next = nxt_node

        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        curr = self.dummy
        while curr.next:
            curr = curr.next
        curr.next = new_node

        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        
        ind = 0
        curr = self.dummy

        while curr and curr.next:
            if ind == index:
                break
            curr = curr.next
            ind += 1
        
        curr.next = curr.next.next
        
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.dummy.next

        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
