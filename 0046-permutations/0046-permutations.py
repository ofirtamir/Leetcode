class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        h= []
        def dfs(h):
            if len(h) == len(nums):
                res.append(h.copy())
                return
            for n in nums:
                if n not in h:
                    h.append(n)
                    dfs(h)
                    h.pop()

            
        dfs([])
        return res