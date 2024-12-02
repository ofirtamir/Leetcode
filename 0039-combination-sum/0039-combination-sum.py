class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        h =[]
        res =[]
        def dfs(i):
            if sum(h)== target:
                if h not in res:
                    res.append(h.copy())
                return
            elif i>= len(candidates) or sum(h)> target:
                return 
            h.append(candidates[i])
            dfs(i)
            dfs(i+1)
            h.pop()
            dfs(i+1)

        dfs(0)
        return res