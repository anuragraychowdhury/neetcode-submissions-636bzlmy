class ListNode:
    def __init__(self, key=-1, next=None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.hashSet = [ListNode() for _ in range(10**4)]
        self.size = len(self.hashSet)

    def add(self, key: int) -> None:
        head = self.hashSet[key % self.size]
        
        if self.contains(key) == True:
            return 
        
        curr = head
        while curr.next:
            curr = curr.next
        added = ListNode(key)
        curr.next = added
        return

    def remove(self, key: int) -> None:
        head = self.hashSet[key % self.size]
    
        curr = head
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next 
            else:
                curr = curr.next
        return
        

    def contains(self, key: int) -> bool:
        head = self.hashSet[key % self.size]
    
        curr = head
        while curr.next:
            if curr.next.key == key:
                return True 
            else:
                curr = curr.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)