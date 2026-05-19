class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n
        
        left = 0
        best = 1

        for right in range(1, n):
            if arr[right - 1] == arr[right]:
                left = right
            elif right > 1 and (
                (arr[right - 2] < arr[right - 1] < arr[right]) or
                arr[right - 2] > arr[right - 1] > arr[right]):
                left = right - 1
            best = max(best, right - left + 1)
        return best