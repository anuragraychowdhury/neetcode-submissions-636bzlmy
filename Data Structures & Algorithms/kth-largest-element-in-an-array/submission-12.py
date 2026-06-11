import random 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(left, right):
            if left >= right:
                return
            low = left
            high = right
            pivot_val = nums[right]

            i = left
            while i <= high:
                if nums[i] < pivot_val:
                    nums[low], nums[i] = nums[i], nums[low]
                    low += 1
                    i += 1
                elif nums[i] > pivot_val:
                    nums[i], nums[high] = nums[high], nums[i]
                    high -= 1
                else:
                    i += 1
            
            if low <= len(nums) - k <= high:
                return 
            elif len(nums) - k < low:
                return quickSelect(left, low - 1)
            else:
                return quickSelect(high + 1, right)
        
        quickSelect(0, len(nums) - 1)
        return nums[len(nums) - k]
            
            


            
            
        
        