class Solution:
    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        parent = {}
        size = {}

        def find(current_node):
            while current_node != parent[current_node]:
                parent[current_node] = parent[parent[current_node]]
                current_node = parent[current_node]
            return current_node
        
        def union(current, neighbor):
            parent_curr = find(current)
            parent_neigh = find(neighbor)

            if parent_curr == parent_neigh:
                return False
            
            if size[parent_neigh] >= size[parent_curr]:
                size[parent_neigh] += size[parent_curr]
                parent[parent_curr] = parent[parent_neigh]
            else:
                size[parent_curr] += size[parent_neigh]
                parent[parent_neigh] = parent[parent_curr]
            
            return True
        
        num_islands = 0
        res = []
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        for x,y in positions:
            if (x,y) in visited:
                res.append(num_islands)
                continue
            
            num_islands += 1
            parent[(x,y)] = (x,y)
            size[(x,y)] = 1
            visited.add((x,y))

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) in visited:
                    if union((x,y), (nx,ny)) == True:
                        num_islands -= 1
            res.append(num_islands)
        return res






                