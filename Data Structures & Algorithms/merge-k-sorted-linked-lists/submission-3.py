# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge_lists(list1, list2):
            dummy = ListNode(0)
            curr = dummy
            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            
            if list1:
                curr.next = list1
            if list2:
                curr.next = list2
            
            return dummy.next
        
        if not lists:
            return None
        
        while len(lists) > 1:
            new_list = []
            for i in range(0, len(lists) - 1, 2):
                first_list = lists[i]
                second_list = lists[i + 1]
                merged = merge_lists(first_list, second_list)
                new_list.append(merged)
            if len(lists) % 2 != 0:
                new_list.append(lists[-1])
            lists = new_list
        return lists[0]
        
                

            
                