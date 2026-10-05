class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        max_freq = 0
        running_sum = 0

        for right in range(len(nums)):
            window_len = (right - left) + 1
            pote_sum = nums[right] * window_len
            running_sum += nums[right]
            increments = pote_sum - running_sum
            if increments > k:
                running_sum -= nums[left]
                left += 1
            max_freq = max(max_freq, right - left + 1)
        return max_freq