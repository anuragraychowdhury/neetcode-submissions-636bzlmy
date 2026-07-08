class ListNode:
    def __init__(self, key, value, prev, next):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.left = ListNode(-1, -1, None, None)
        self.right = ListNode(-1, -1, None, None)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove_node(self, node):
        previous_node = node.prev
        next_node = node.next
        previous_node.next = next_node
        next_node.prev = previous_node
    
    def insert_node_right(self, node):
        previous_node = self.right.prev
        previous_node.next = node
        node.prev = previous_node
        node.next = self.right
        self.right.prev = node
    

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {} # key to node itself; check if node in our data structure
        self.key_to_freq = {} # key to the frequency that it is associated with
        self.freq_to_DLL = defaultdict(DoublyLinkedList) # frequency and the DLL that holds all nodes for that freq
        self.min_freq = 1

    def get(self, key: int) -> int:
        '''
        get node
        get frequency of node
        find linked list associated with that frequency
        remove the node from the linked list
        increment the frequency of use
        if the min frequency DLL is empty, increment min freq
        insert the new node on right (MRU) of new DLL (incremented freq)
        update the key to frequency to hold key : new_frequency
        return the value of the node 
        '''
        if key in self.key_to_node:
            curr_node = self.key_to_node[key]
            curr_frequency = self.key_to_freq[key]
            linked_list = self.freq_to_DLL[curr_frequency]
            linked_list.remove_node(curr_node)

            if curr_frequency == self.min_freq and linked_list.left.next == linked_list.right:
                self.min_freq += 1

            curr_frequency += 1 
            self.freq_to_DLL[curr_frequency].insert_node_right(curr_node)
            self.key_to_freq[key] = curr_frequency
            return self.key_to_node[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        '''
        if key is present:
            get the node value
            get the current frequency
            get the linked list that it is in
            remove the node from the linked list
            increment the frequency that it is in 
            if the linked list of that frequency is None, increment the max frequency
            insert the node into the new linked list
            update the frequency
            update the value
            return
        otherwise:
            if we are at capacity:
                remove the LRU node from the min_freq linked list
            if we are not at capacity:
                create the new node
                add it to the right side of the min_freq (since this is the first time the node is being used)
                update all necessary dicts 
                return the value
        '''
        if key in self.key_to_node:
            curr_node = self.key_to_node[key]
            curr_frequency = self.key_to_freq[key]
            linked_list = self.freq_to_DLL[curr_frequency]
            linked_list.remove_node(curr_node)

            if curr_frequency == self.min_freq and linked_list.left.next == linked_list.right:
                self.min_freq += 1

            curr_frequency += 1             
            self.freq_to_DLL[curr_frequency].insert_node_right(curr_node)
            self.key_to_freq[key] = curr_frequency
            self.key_to_node[key].value = value
            return 
        else:
            if len(self.key_to_node) == self.capacity:
                linked_list = self.freq_to_DLL[self.min_freq]
                LRU = linked_list.left.next
                linked_list.remove_node(LRU)
                del self.key_to_node[LRU.key]
                del self.key_to_freq[LRU.key]
            new_node = ListNode(key, value, None, None)
            self.min_freq = 1
            self.freq_to_DLL[self.min_freq].insert_node_right(new_node)
            self.key_to_node[key] = new_node
            self.key_to_freq[key] = self.min_freq
            return 
                

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)