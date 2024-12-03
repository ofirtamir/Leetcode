class Solution:
    def rob(self, nums: List[int]) -> int:
        # x=0
        # y=0
        # if len(nums)%2 !=0:
        #     nums.append(0)
        # for i in range(0, len(nums)-1, 2):
        #     x+= nums[i]
        #     y+= nums[i+1]
        # return max(x,y)

        # def dfs(nums,i):
        #     if i >= len(nums):
        #         return 0
        #     return max(dfs(nums,i+1),nums[i] + dfs(nums,i+2))
        # return dfs(nums,0)
        rob1= 0
        rob2= 0
        for n in nums:
            t= max(rob2, rob1+ n)
            rob1 =rob2
            rob2= t
        return rob2