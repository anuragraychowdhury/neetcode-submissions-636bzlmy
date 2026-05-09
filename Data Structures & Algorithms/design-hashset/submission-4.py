class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.hashSet = [Node() for i in range(10**5)]
        self.size = len(self.hashSet)
    
    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        
        index = self._hash(key)
        linked_list = self.hashSet[index]
        curr = linked_list

        while curr.next:
            curr = curr.next
        curr.next = Node(key)

        return

    def remove(self, key: int) -> None:
        index = self._hash(key)
        linked_list = self.hashSet[index]
        curr = linked_list

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        
        return

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        linked_list = self.hashSet[index]
        curr = linked_list

        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        
        return False