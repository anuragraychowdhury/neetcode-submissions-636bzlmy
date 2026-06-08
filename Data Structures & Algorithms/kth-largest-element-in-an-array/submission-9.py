import random 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(left, right):
            low = left
            high = right

            pivot_index = right 
            pivot_value = nums[right]

            i = left
            while i <= high:
                if nums[i] < pivot_value:
                    nums[low], nums[i] = nums[i], nums[low]
                    low += 1
                    i += 1
                elif nums[i] > pivot_value:
                    nums[i], nums[high] = nums[high], nums[i]
                    high -= 1
                else:
                    i += 1
            return (low, high)
    

        def quickSelect(left, right):
            if left >= right:
                return nums[left]
            
            lower_bound, upper_bound = partition(left, right)
            if lower_bound <= len(nums) - k <= upper_bound:
                return nums[len(nums) - k]
            elif len(nums) - k < lower_bound:
                return quickSelect(left, lower_bound - 1)
            else:
                return quickSelect(upper_bound + 1, right)
        
        return quickSelect(0, len(nums) - 1)


            
            
        
        