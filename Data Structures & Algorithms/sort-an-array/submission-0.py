class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(lst1, lst2):
            i = 0
            j = 0 
            sorted_list = []
            while i < len(lst1) and j < len(lst2):
                if lst1[i] <= lst2[j]:
                    sorted_list.append(lst1[i])
                    i += 1
                else:
                    sorted_list.append(lst2[j])
                    j += 1
            
            if i < len(lst1):
                sorted_list.extend(lst1[i:])
            if j < len(lst2):
                sorted_list.extend(lst2[j:])
            return sorted_list
        
        if len(nums) <= 1:
            return nums
        
        partition = len(nums) // 2
        first_half = self.sortArray(nums[:partition])
        second_half = self.sortArray(nums[partition:])
        
        return merge(first_half, second_half)
