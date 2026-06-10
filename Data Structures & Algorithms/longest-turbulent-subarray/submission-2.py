class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return 1
        
        left = 0
        longest = 1
        for right in range(1, len(arr)):
            if arr[right] == arr[right - 1]:
                left = right
            elif right >= 2: 
                if (arr[right - 2] < arr[right - 1] and arr[right - 1] < arr[right]) or (arr[right - 2] > arr[right - 1] and arr[right - 1] > arr[right]):
                    left = right - 1
            longest = max(longest, right - left + 1)
        return longest
            