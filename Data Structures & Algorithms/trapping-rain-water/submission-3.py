class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = 0
        max_right = 0
        left = 0
        right = len(height) - 1
        water = 0

        while left < right:
            max_left = max(height[left], max_left)
            max_right = max(height[right], max_right)
            if height[left] <= height[right]:
                water += min(max_left, max_right) - height[left]
                left += 1
            else:
                water += min(max_left, max_right) - height[right]
                right -= 1
        return water