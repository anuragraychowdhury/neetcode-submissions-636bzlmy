class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        running_sum = 0
        left = 0
        total = 0
        for right in range(len(arr)):
            running_sum += arr[right]
            if right - left + 1 == k:
                if running_sum // k >= threshold:  # Fix: >= not <=
                    total += 1
                running_sum -= arr[left]
                left += 1
        return total