class ListNode:
    def __init__(self, key=-1, value=-1, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.left_node = ListNode()
        self.right_node = ListNode()
        self.left_node.next = self.right_node
        self.right_node.prev = self.left_node
        self.size = 0
        self.capacity = capacity
        self.key_check = {}
    
    def remove_node(self, node):
        previous_node = node.prev
        next_node = node.next
        previous_node.next = next_node
        next_node.prev = previous_node

        self.size -= 1
    
    def insert_node_right(self, key, value):
        last_node = self.right_node.prev
        new_node = ListNode(key, value)
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.right_node
        self.right_node.prev = new_node

        self.size += 1
        return new_node

    def get(self, key: int) -> int:
        if key in self.key_check:
            val = self.key_check[key].value
            self.remove_node(self.key_check[key])
            new_node = self.insert_node_right(key, val)
            self.key_check[key] = new_node
            return new_node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_check:
            self.key_check[key].value = value
            self.remove_node(self.key_check[key])
            new_node = self.insert_node_right(key, self.key_check[key].value)
            self.key_check[key] = new_node
            return
        else:
            new_node = ListNode(key, value)
        
        if self.size == self.capacity:
            LRU_node = self.left_node.next
            self.remove_node(LRU_node)
            del self.key_check[LRU_node.key]
        
        newly_put_node = self.insert_node_right(new_node.key, new_node.value)
        self.key_check[key] = newly_put_node
        return 




