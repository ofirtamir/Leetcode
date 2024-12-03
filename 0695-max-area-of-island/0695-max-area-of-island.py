class Solution:
    def dfs(self,grid,r,c):
        if r<0 or r >= len(grid) or c < 0 or c>=len(grid[0]) or grid[r][c]==0:
            return 0
        grid[r][c]=0
        # n+=1
        # n+=self.dfs(grid,r+1,c,0)
        # n+=self.dfs(grid,r-1,c,0)
        # n+=self.dfs(grid,r,c+1,0)
        # n+=self.dfs(grid,r,c-1,0)
        # return n
        return 1+ self.dfs(grid,r+1,c) +self.dfs(grid,r-1,c)+ self.dfs(grid,r,c+1) +self.dfs(grid,r,c-1) 
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    m= max(m, self.dfs(grid, r, c))
        return m