class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # def dfs(nums,i):
        #     if i >= len(nums)-1:
        #         return True
        #     for x in range(1,nums[i]+1):
        #         if dfs(nums,i+x):
        #             return True
        #     return False
        # if len(nums)==1:
        #     return True
        # return dfs(nums,0)
        gol= len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=gol:
                gol= i
        return gol==0