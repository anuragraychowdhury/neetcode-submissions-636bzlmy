class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {i: [] for i in range(n + 1)}

        for node1, node2, time in times:
            edges[node1].append((time, node2))
        
        res = 0
        visit = set()
        minHeap = [(0, k)]

        while minHeap:
            time, node1 = heapq.heappop(minHeap)
            if node1 in visit:
                continue
            visit.add(node1)
            res = max(res, time)

            for time2,node2 in edges[node1]:
                if node2 not in visit:
                    heapq.heappush(minHeap, (time2 + time, node2))
        
        return res if len(visit) == n else -1