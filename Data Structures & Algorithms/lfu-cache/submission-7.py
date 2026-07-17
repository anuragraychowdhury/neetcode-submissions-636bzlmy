class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        left_node = node.prev
        right_node = node.next
        left_node.next = right_node
        right_node.prev = left_node
    
    def insert_right(self, node):
        previous_node = self.right.prev
        node.prev = previous_node
        previous_node.next = node
        node.next = self.right
        self.right.prev = node
    
    def is_empty(self):
        return self.left.next == self.right

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 1
        self.key_to_node = {}
        self.key_to_freq = {}
        self.freq_to_DLL = {}

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            freq = self.key_to_freq[key]
            DLL = self.freq_to_DLL[freq]
            DLL.remove(self.key_to_node[key])
            
            if freq == self.min_freq and DLL.is_empty():
                self.min_freq += 1
            freq += 1
            self.key_to_freq[key] = freq
            
            if freq not in self.freq_to_DLL:
                self.freq_to_DLL[freq] = DoublyLinkedList()
            
            new_DLL = self.freq_to_DLL[freq]
            new_DLL.insert_right(self.key_to_node[key])
            return self.key_to_node[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.key_to_node[key].val = value
            freq = self.key_to_freq[key]
            DLL = self.freq_to_DLL[freq]
            DLL.remove(self.key_to_node[key])
            
            if freq == self.min_freq and DLL.is_empty():
                self.min_freq += 1
            freq += 1
            self.key_to_freq[key] = freq
            
            if freq not in self.freq_to_DLL:
                self.freq_to_DLL[freq] = DoublyLinkedList()
            
            new_DLL = self.freq_to_DLL[freq]
            new_DLL.insert_right(self.key_to_node[key])
        else:
            if len(self.key_to_node) == self.capacity:
                min_DLL = self.freq_to_DLL[self.min_freq]
                LRU = min_DLL.left.next
                min_DLL.remove(LRU)
                del self.key_to_node[LRU.key]
                del self.key_to_freq[LRU.key]
            
            self.min_freq = 1
            if self.min_freq not in self.freq_to_DLL:
                self.freq_to_DLL[self.min_freq] = DoublyLinkedList()
            
            new_node = ListNode(key, value)
            self.freq_to_DLL[self.min_freq].insert_right(new_node)
            self.key_to_node[key] = new_node
            self.key_to_freq[key] = self.min_freq

            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)