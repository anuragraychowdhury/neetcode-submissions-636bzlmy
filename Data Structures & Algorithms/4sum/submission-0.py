class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    quad = nums[i] + nums[j] + nums[left] + nums[right]
                    if quad == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        curr_left = nums[left]
                        curr_right = nums[right]

                        while left < right and nums[left] == curr_left:
                            left += 1
                        while left < right and nums[right] == curr_right:
                            right -= 1
                    elif quad > target:
                        right -= 1
                    else:
                        left += 1
        return res