class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()
        max_heap = []

        task_freq = {}
        for task in tasks:
            task_freq[task] = task_freq.get(task, 0) + 1
        
        for task, freq in task_freq.items():
            heapq.heappush(max_heap, (-freq, task))
        
        time = 0
        while queue or max_heap:
            while queue and queue[0][1] == time:
                task, time_avail, freq = queue.popleft()
                heapq.heappush(max_heap, (freq, task))
            
            if max_heap:
                f,t = heapq.heappop(max_heap)
                if f != -1:
                    next_time = time + n + 1
                    updated_freq = f + 1
                    queue.append((task, next_time, updated_freq))
            time += 1
        return time