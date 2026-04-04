class ListNode:
    def __init__(self,key=-1,value=-1,next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.hashMap = [ListNode() for _ in range(10**4)]
        self.size = len(self.hashMap)

    def put(self, key: int, value: int) -> None:
        head = self.hashMap[key % self.size]

        curr = head
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            else:
                curr = curr.next
        added = ListNode(key, value)
        curr.next = added

    def get(self, key: int) -> int:
        head = self.hashMap[key % self.size]

        curr = head
        while curr.next:
            if curr.next.key == key:
                return curr.next.value
            else:
                curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        head = self.hashMap[key % self.size]

        curr = head
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            else:
                curr = curr.next
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)