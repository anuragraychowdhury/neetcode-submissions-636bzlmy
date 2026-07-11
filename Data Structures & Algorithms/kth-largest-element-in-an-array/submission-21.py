class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickSelect(left, right):
            if left >= right:
                return
            
            dupe_low_bound = left
            dupe_high_bound = right
            pivot_value = nums[right]
            i = left

            while i <= dupe_high_bound:
                if nums[i] < pivot_value:
                    nums[i], nums[dupe_low_bound] = nums[dupe_low_bound], nums[i]
                    dupe_low_bound += 1
                    i += 1
                elif nums[i] > pivot_value:
                    nums[i], nums[dupe_high_bound] = nums[dupe_high_bound], nums[i]
                    dupe_high_bound -= 1
                else:
                    i += 1
            
            target_index = len(nums) - k
            if dupe_low_bound <= target_index <= dupe_high_bound:
                return 
            elif target_index < dupe_low_bound:
                return quickSelect(left, dupe_low_bound - 1)
            else:
                return quickSelect(dupe_high_bound + 1, right)
        
        quickSelect(0, len(nums) - 1)
        return nums[len(nums) - k]
            