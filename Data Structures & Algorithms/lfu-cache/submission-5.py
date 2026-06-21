class ListNode:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0
    
    def remove_node(self, node):
        previous_node = node.prev
        next_node = node.next
        previous_node.next = next_node
        next_node.prev = previous_node
        self.size -= 1
    
    def insert_right(self, node):
        last_node = self.right.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.right
        self.right.prev = node
        self.size += 1

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.lowest_freq = 1
        self.freq_to_DLL = {}
        self.key_to_freq = {}
    
    def get(self, key: int) -> int:
        if key in self.key_to_node:
            key_freq = self.key_to_freq[key]
            self.freq_to_DLL[key_freq].remove_node(self.key_to_node[key])
            if self.freq_to_DLL[key_freq].size == 0 and key_freq == self.lowest_freq:
                self.lowest_freq += 1

            key_freq += 1
            if key_freq not in self.freq_to_DLL:
                self.freq_to_DLL[key_freq] = DLL()
            self.freq_to_DLL[key_freq].insert_right(self.key_to_node[key])
            self.key_to_freq[key] = key_freq
            return self.key_to_node[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.key_to_node[key].value = value
            key_freq = self.key_to_freq[key]
            
            self.freq_to_DLL[key_freq].remove_node(self.key_to_node[key])
            if self.freq_to_DLL[key_freq].size == 0 and key_freq == self.lowest_freq:
                self.lowest_freq += 1
            
            key_freq += 1
            if key_freq not in self.freq_to_DLL:
                self.freq_to_DLL[key_freq] = DLL()
            self.freq_to_DLL[key_freq].insert_right(self.key_to_node[key])
            self.key_to_freq[key] = key_freq
            return
        else:
            new_node = ListNode(key, value)
            if len(self.key_to_node) == self.capacity:
                LFU_DLL = self.freq_to_DLL[self.lowest_freq]
                LRU_node = LFU_DLL.left.next
                LFU_DLL.remove_node(LRU_node)
                del self.key_to_node[LRU_node.key]
                del self.key_to_freq[LRU_node.key]

                if self.freq_to_DLL[self.lowest_freq].size == 0:
                    self.lowest_freq += 1
            
            self.lowest_freq = 1
            if self.lowest_freq not in self.freq_to_DLL:
                self.freq_to_DLL[self.lowest_freq] = DLL()

            self.freq_to_DLL[self.lowest_freq].insert_right(new_node)
            self.key_to_freq[key] = self.lowest_freq
            self.key_to_node[key] = new_node
        return 

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)