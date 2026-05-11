class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                triplet = nums[i] + nums[left] + nums[right]
                if triplet == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    
                    curr_left = nums[left]
                    curr_right = nums[right]

                    while left < right and nums[left] == curr_left:
                        left += 1
                    while right > left and nums[right] == curr_right:
                        right -= 1
                
                elif triplet > 0:
                    right -= 1
                else:
                    left += 1
        return res