class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        slow marks where we need to overwrite
        fast does the searching
        if fast != value, swap slow value with fast and then increment slow
        otherwise, if fast == value, dont move slow
        '''
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return slow