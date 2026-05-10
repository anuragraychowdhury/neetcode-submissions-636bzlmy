class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            correct_index = nums[i]
            if correct_index < len(nums) + 1 and nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return nums[i]