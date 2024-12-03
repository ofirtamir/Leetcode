class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1=0
        rob2=0
        rob22=0
        rob11=0
        for i in range(1,len(nums)):
            t1= max(rob2,rob1+nums[i])
            rob1=rob2
            rob2=t1
        for x in range(0,len(nums)-1):
            t2= max(rob22,rob11+nums[x])
            rob11=rob22
            rob22=t2
        return nums[0] if len(nums)==1 else max(rob22,rob2)
