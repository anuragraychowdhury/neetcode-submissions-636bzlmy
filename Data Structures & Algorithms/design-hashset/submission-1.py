'''
create a list of dummy nodes where each index is a dummy node of a linked list. the reason using a linked list here is advantageous is because it lets us have an O(1) add and we do not have to shift the entire array upon removal; we can just rewire it

[ListNode(-1,-1), ListNode(-1,-1), ListNode(-1,-1)]
adding -> check whether the current list contains the node already. if it does, return. otherwise add it to the end of the linked list and then return
removing -> iterate through the current list and then check if node.next is the value we are looking for. if it is, rewire it to skip that node and return
contains -> determine whether a node exists by checking if node.next is the value we are looking for or not
'''

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