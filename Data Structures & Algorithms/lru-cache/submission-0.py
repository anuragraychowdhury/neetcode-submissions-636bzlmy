class ListNode:
    def __init__(self, key, value, next, prev):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = ListNode(-1, -1, None, None)
        self.right = ListNode(-1, -1, None,None)
        self.left.next = self.right
        self.right.prev = self.left
        self.node_dict = {}
    
    def insert_at_front(self,node):
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node
    
    def remove(self,node):
        left_node = node.prev
        right_node = node.next
        left_node.next = right_node
        right_node.prev = left_node

    def get(self, key: int) -> int:
        if key in self.node_dict:
            found_node = self.node_dict[key]
            self.remove(found_node)
            self.insert_at_front(found_node)
            return found_node.value
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.node_dict:
            self.node_dict[key].value = value
            updated_node = self.node_dict[key]
            self.remove(updated_node)
            self.insert_at_front(updated_node)
            return
        
        if len(self.node_dict) == self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            del self.node_dict[LRU.key]
        new_node = ListNode(key, value, None, None)
        self.insert_at_front(new_node)
        self.node_dict[key] = new_node
        return 