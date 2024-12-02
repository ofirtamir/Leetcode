class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        h =[]
        res =[]
        def dfs(i):
            x=sum(h)
            if x== target:
                if h not in res:
                    res.append(h.copy())
                return
            elif i>= len(candidates) or x> target:
                return 
            h.append(candidates[i])
            dfs(i)
            h.pop()
            dfs(i+1)

        dfs(0)
        return res