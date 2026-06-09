class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_to_index = {0:-1}
        running_sum = 0
        for right in range(len(nums)):
            running_sum += nums[right]
            if running_sum % k in remainder_to_index:
                if right - remainder_to_index[running_sum % k] >= 2:
                    return True
            else:
                remainder_to_index[running_sum % k] = right
        return False
            