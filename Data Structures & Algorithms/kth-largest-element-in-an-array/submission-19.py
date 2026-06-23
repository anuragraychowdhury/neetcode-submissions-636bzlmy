class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickSelect(left, right):
            if left >= right:
                return left
            
            frontier = left
            pivot = nums[right]
            high_ptr = right

            i = left
            while i <= high_ptr:
                if nums[i] < pivot:
                    nums[i], nums[frontier] = nums[frontier], nums[i]
                    frontier += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[high_ptr] = nums[high_ptr], nums[i]
                    high_ptr -= 1
                else:
                    i += 1
            
            target = len(nums) - k
            if frontier <= target <= high_ptr:
                return frontier
            elif target < frontier:
                return quickSelect(left, frontier - 1)
            else:
                return quickSelect(frontier + 1, right)
        
        index = quickSelect(0, len(nums) - 1)
        return nums[index]

