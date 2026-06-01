class ListNode:
    def __init__(self, key, value, prev, next):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.left = ListNode(None,None,None,None)
        self.right = ListNode(None,None,None,None)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self,node):
        left_node = node.prev
        right_node = node.next
        left_node.next = right_node
        right_node.prev = left_node
        return 
    
    def insert_at_front(self,node):
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node
        return 
    
    def is_empty(self):
        return self.left.next == self.right

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.key_to_freq = {}
        self.freq_to_DLL = defaultdict(DoublyLinkedList)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            curr_node = self.key_to_node[key]
            curr_freq = self.key_to_freq[key]
            
            self.freq_to_DLL[curr_freq].remove(curr_node)
            if self.freq_to_DLL[curr_freq].is_empty() and curr_freq == self.min_freq:
                self.min_freq += 1
            
            self.key_to_freq[key] = curr_freq + 1
            self.freq_to_DLL[curr_freq + 1].insert_at_front(curr_node)

            return curr_node.value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            curr_node = self.key_to_node[key]
            curr_freq = self.key_to_freq[key]
            curr_node.value = value
            
            self.freq_to_DLL[curr_freq].remove(curr_node)
            if self.freq_to_DLL[curr_freq].is_empty() and curr_freq == self.min_freq:
                self.min_freq += 1
            
            self.key_to_freq[key] = curr_freq + 1
            self.freq_to_DLL[curr_freq + 1].insert_at_front(curr_node)

            return
        
        if len(self.key_to_node) == self.capacity:
            LRU_LL = self.freq_to_DLL[self.min_freq]
            LRU_node = LRU_LL.left.next
            LRU_LL.remove(LRU_node)
            del self.key_to_node[LRU_node.key]
            del self.key_to_freq[LRU_node.key]
        
        new_node = ListNode(key, value, None, None)
        self.key_to_node[key] = new_node
        self.key_to_freq[key] = 1
        self.freq_to_DLL[1].insert_at_front(new_node)
        self.min_freq = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)