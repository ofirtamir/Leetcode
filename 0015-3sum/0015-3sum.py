class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res =defaultdict(set)
        # for i in range(len(nums)):
        #     for x in range(i+1, len(nums)):
        #         for y in range(x+1,len(nums)):
        #             if (i==x or i == y or x==y):
        #                 continue
        #             if nums[i] + nums[x] + nums[y] == 0 :
        #                 l=[nums[i],nums[x],nums[y]].sort()
        #                 res[l](l)

        # return list(res)
        res =[]
        nums.sort()
        for i ,a in enumerate(nums) :
            if a>0:
                break
            if i > 0 and a == nums[i-1] :
                continue
            l = i+1
            r =len(nums) -1
            
            while l < r :
                q= a+ nums[l] +nums[r]
                if q > 0 :
                    r= r -1 
                elif q < 0 :
                    l = l + 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l]==nums[l-1] and l< r :
                        l= l+1 

        return res