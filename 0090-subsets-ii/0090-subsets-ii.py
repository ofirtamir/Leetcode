class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        h =[]
        res =[]
        nums.sort()
        def dfs(i):
            if i==len(nums):
                if h not in res:
                    res.append(h.copy())
                    return
                else:
                    return 
            h.append(nums[i])
            dfs(i+1)
            h.pop()
            dfs(i+1)

        dfs(0)
        return res
        