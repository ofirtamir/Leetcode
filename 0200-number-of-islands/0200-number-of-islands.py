class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     if not grid:
    #         return 0
    #     rows, cols = len(grid), len(grid[0])
    #     res=0
    #     visit = set()

    #     def bfs(r, c):
    #         q = collections.deque()
    #         visit.add((r,c))
    #         q.append((r,c))
    #         while q:
    #             row , col = q.popleft()
    #             directions = [[1,0],[-1,0],[0,1],[0,-1]]
    #             for dr, dc in directions:
    #                 r, c = row +dr, col+ dc
    #                 if ( r in range(rows) and c in range(cols) and grid[r][c] =="1" and (r,c) not in visit):
    #                     q.append((r,c))
    #                     visit.add((r,c))
    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c] == "1" and (r,c) not in visit:
    #                 bfs(r,c)
    #                 res+= 1

    #     return res
    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count