class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for index, task in enumerate(tasks):
            task.append(index)
        
        tasks.sort(key=lambda x: x[0])
        min_heap = []

        i = 0
        time = tasks[0][0]
        res = []

        while i < len(tasks) or min_heap:
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if min_heap:
                processing_time, task_index = heapq.heappop(min_heap)
                time += processing_time
                res.append(task_index)
            else:
                time = tasks[i][0]
        return res