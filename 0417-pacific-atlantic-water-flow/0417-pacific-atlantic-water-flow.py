class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row,col = len(heights),len(heights[0])
        p ,o = set(),set()
        res=[]
        def dfs(r,c,visit,per):
            if r<0 or c<0 or r==row or c==col or (r,c) in visit or heights[r][c]< per:
                return 
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        for c in range(col):
            dfs(0,c,p,heights[0][c])
            dfs(row-1,c,o,heights[row-1][c])
        for r in range(row):
            dfs(r,0,p,heights[r][0])
            dfs(r,col-1,o,heights[r][col-1])
        for r in range(row):
            for c in range(col):
                if (r,c) in p and (r,c) in o:
                    res.append([r,c])
        return res
