class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        max_window = 0
        window_sum = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            while (nums[right] * (right - left + 1)) - window_sum > k:
                window_sum -= nums[left]
                left += 1
            
            max_window = max(right - left + 1, max_window)
        return max_window