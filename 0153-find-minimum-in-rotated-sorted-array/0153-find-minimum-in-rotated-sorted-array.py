class Solution:
    def findMin(self, nums: List[int]) -> int:
        res =nums[0]
        l ,r = 0, len(nums)-1

        while l<=r:
            m= (l+r)//2
            if nums[m] >= nums[l]:
                res= min(res,nums[l],nums[m])
                l= m+1
            else:
                res= min(res,nums[r],nums[m])
                r = m-1
        return res