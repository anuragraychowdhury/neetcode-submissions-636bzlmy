class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_q = deque()
        left = 0
        res = []

        for right in range(len(nums)):
            if mono_q and mono_q[0][0] < left:
                mono_q.popleft()
            while mono_q and nums[right] > mono_q[-1][1]:
                mono_q.pop()
            mono_q.append((right, nums[right]))

            if right - left + 1 == k:
                res.append(mono_q[0][1])
                left += 1
        return res
