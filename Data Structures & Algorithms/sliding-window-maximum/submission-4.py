class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_queue = deque() # index, value
        left = 0
        res = []
        
        for i in range(len(nums)):
            while mono_queue and mono_queue[0][0] < left:
                mono_queue.popleft()
            
            while mono_queue and nums[i] >= mono_queue[-1][1]:
                mono_queue.pop()
            
            mono_queue.append((i, nums[i]))

            if i - left + 1 == k:
                res.append(mono_queue[0][1])
                left += 1
        
        return res
            
                 