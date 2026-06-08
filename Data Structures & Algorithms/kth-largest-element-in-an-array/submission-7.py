import random 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(left, right):
            i = left
            pivot_index = random.randint(left, right)
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            for j in range(left, right):
                if nums[j] <= nums[right]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i +=1 
            nums[i], nums[right] = nums[right], nums[i]
            return i

        def quickSelect(left, right):
            if left >= right:
                return left
            
            pivot_index = partition(left, right)
            if pivot_index == len(nums) - k:
                return pivot_index
            elif pivot_index > len(nums) - k:
                return quickSelect(left, pivot_index - 1)
            else:
                return quickSelect(pivot_index + 1, right)
            
        pivot = quickSelect(0, len(nums) - 1)
        return nums[pivot]
            
            
        
        