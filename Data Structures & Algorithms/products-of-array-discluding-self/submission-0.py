class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left  = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i+1] * right[i + 1]
        print(left)
        print(right)
        res = [1] * len(nums)

        for i in range(len(res)):
            res[i] = left[i] * right[i]
        
        return res
