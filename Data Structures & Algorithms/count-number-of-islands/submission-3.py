class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        parent_dict = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    parent_dict[(i,j)] = (i,j)
        
        def find(node):
            if node != parent_dict[node]:
                parent_dict[node] = parent_dict[parent_dict[node]]
                node = find(parent_dict[node])
            return node
        
        def union(curr_node, comp_node):
            curr_parent = find(curr_node)
            comp_parent = find(comp_node)

            if curr_parent == comp_parent:
                return 
            
            parent_dict[comp_parent] = parent_dict[curr_parent]
            return 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j < len(grid[0]) - 1 and grid[i][j] == '1' and grid[i][j + 1] == '1':
                    union((i,j), (i,j+1))
                if i < len(grid) - 1 and grid[i][j] == '1' and grid[i + 1][j] == '1':
                    union((i,j), (i+1,j))
        
        components = set()
        for cell in parent_dict:
            par = find(cell)
            components.add(par)
        
        return len(components)
                

        
