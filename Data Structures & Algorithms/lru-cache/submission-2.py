class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.left = ListNode(-1, -1)
        self.right = ListNode(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert_right(self, node):
        prev_node = self.right.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        self.right.prev = node
        return
    
    def remove_node(self, node):
        prev_node = node.prev
        prev_node.next = node.next
        node.next.prev = prev_node
        return

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            self.remove_node(self.key_to_node[key])
            self.insert_right(self.key_to_node[key])
            return self.key_to_node[key].value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.remove_node(self.key_to_node[key])
            self.insert_right(self.key_to_node[key])
            self.key_to_node[key].value = value
            return
        else:
            if len(self.key_to_node) == self.capacity:
                LRU = self.left.next
                self.remove_node(LRU)
                del self.key_to_node[LRU.key]
            new_node = ListNode(key, value)
            self.insert_right(new_node)
            self.key_to_node[key] = new_node
        return


            
        
