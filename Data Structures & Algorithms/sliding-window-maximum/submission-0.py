class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_q = deque() # (value, index)
        left = 0
        res = []

        for right in range(len(nums)):
            
            while len(mono_q) > 0 and nums[right] > mono_q[-1][0]:
                mono_q.pop()
            mono_q.append((nums[right], right))
            
            if len(mono_q) > 0 and left > mono_q[0][1]:
                mono_q.popleft()
            if len(mono_q) > 0 and (right - left + 1) == k:
                res.append(mono_q[0][0])
                left += 1
            
        return res