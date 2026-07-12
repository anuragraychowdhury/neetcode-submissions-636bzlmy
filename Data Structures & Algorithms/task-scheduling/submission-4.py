class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = {}
        for task_letter in tasks:
            task_freq[task_letter] = task_freq.get(task_letter, 0) + 1
        
        max_heap = []
        for letter, freq in task_freq.items():
            heapq.heappush(max_heap, (-freq, letter))
        
        q = deque()
        time = 0

        while max_heap or q:
            
            while q and q[0][0] == time:
                time_ready, freq, letter = q.popleft()
                heapq.heappush(max_heap, (freq, letter))
            
            if max_heap:
                freq, letter = heapq.heappop(max_heap)
                if freq + 1 != 0:
                    q.append((time + n + 1, freq + 1, letter))

            time += 1
        return time 
            
        
