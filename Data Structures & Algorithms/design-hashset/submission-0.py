class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.HashSet = [ListNode(-1) for _ in range(10**4)]
        self.size = len(self.HashSet)

    def add(self, key: int) -> None:
        curr_index = key % self.size
        curr_list = self.HashSet[curr_index]
        
        if self.contains(key):
            return
        curr_iter = curr_list
        
        while curr_iter.next:
            curr_iter = curr_iter.next
        curr_iter.next = ListNode(key)
        return

    def remove(self, key: int) -> None:
        curr_index = key % self.size
        curr_list = self.HashSet[curr_index]
        curr_iter = curr_list
        
        while curr_iter and curr_iter.next:
            if curr_iter.next.val == key:
                curr_iter.next = curr_iter.next.next
                return
            curr_iter = curr_iter.next
        return

    def contains(self, key: int) -> bool:
        curr_index = key % self.size
        curr_list = self.HashSet[curr_index]
        curr_iter = curr_list
        
        while curr_iter.next:
            if curr_iter.next.val == key:
                return True
            curr_iter = curr_iter.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)