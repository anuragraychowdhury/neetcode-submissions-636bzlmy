class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        z = 0
        t = len(nums) - 1

        while c <= t:
            if nums[c] == 0:
                nums[c], nums[z] = nums[z], nums[c]
                z += 1
                c += 1
            elif nums[c] == 2:
                nums[c], nums[t] = nums[t], nums[c]
                t -= 1
            else:
                c += 1