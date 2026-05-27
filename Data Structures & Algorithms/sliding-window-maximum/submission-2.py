class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_queue = deque() # (index, value) -> decreasing
        left = 0
        res = []

        for right in range(len(nums)):
            while mono_queue and mono_queue[-1][1] < nums[right]:
                mono_queue.pop()
            mono_queue.append((right, nums[right]))

            while mono_queue and mono_queue[0][0] < left:
                mono_queue.popleft()

            if right - left + 1 == k:
                res.append(mono_queue[0][1])
                left += 1
        return res

