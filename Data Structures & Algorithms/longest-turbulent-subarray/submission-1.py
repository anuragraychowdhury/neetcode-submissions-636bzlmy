class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        longest = 1

        for right in range(1, n):
            if arr[right] == arr[right - 1]:
                left = right
            
            elif right >= 2:
                if (arr[right] > arr[right - 1] and arr[right - 1] > arr[right - 2]) or (arr[right] < arr[right - 1] and arr[right - 1] < arr[right - 2]):
                    left = right - 1

            longest = max(longest, right - left + 1)
        return longest