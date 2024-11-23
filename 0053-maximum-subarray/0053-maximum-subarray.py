class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return nums[0]
        # dic = {}
        # for i in range(len(nums)):
        #     s= nums[i]
        #     for x in range(i+1, len(nums)):
        #         s+= nums[x]
        #         dic[(i,x)]=s
        # return max(max(dic.values()),max(nums))
        
        # n, res = len(nums), nums[0]
        # for i in range(len(nums)):
        #     cur=0
        #     for x in range(i,len(nums)):
        #         cur+=nums[x]
        #         res =max(res, cur)
        # return res

        maxsum ,cur =nums[0] ,0
        for num in nums:
            if cur< 0:
                cur=0
            cur+= num
            maxsum= max(cur, maxsum)
        return maxsum
        