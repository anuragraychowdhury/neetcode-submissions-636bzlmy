'''
if we split the array in half, there will be a sorted section and an unsorted section (unless the entire array is sorted already)

if we have a situation where it is already sorted, left, middle, right will all be in increasing order where left will be the min

if we have a situation where left < middle but middle > right, we know that the minimum is stored in the unsorted section

if we have a situation where middle < right but left > middle, we know that the minimum is stored in the left section. 

depending on where in the array we are, we can keep the middle as the current smallest value and then move the search space depending on whether middle is in the sorted or unsorted section and keep updating it
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_value = float('inf')

        while left <= right:
            middle = (left + right) // 2
            if nums[left] <= nums[right]:
                return min(min_value, nums[left])
            elif nums[left] > nums[middle]:
                min_value = min(nums[middle], min_value)
                right = middle - 1
            else:
                min_value = min(nums[middle], min_value)
                left = middle + 1
        return min_value

            
            
