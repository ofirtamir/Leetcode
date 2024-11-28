class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # res= -1
        # l, r = 0, len(nums)-1
        # while l<=r:
        #     m= (l+r)//2
        #     if nums[m]== target:
        #         return m
        #     if nums[l]<nums[r]:
        #         if nums[m] > target:
        #             r = m-1
        #             continue
        #         else:
        #             l =m +1
        #             continue
        #     if nums[l]==target:
        #         return l
        #     if nums[r] == target:
        #         return r
        #     if nums[m] > target and nums[l]> target:
        #         l= m + 1
        #     elif nums[m] < target and nums[l] > target:
        #         l = m + 1
        #     elif nums[m] < target and nums[l] < target:
        #         l = m + 1
        #     else:
        #         r= m-1
        # return res
        res =-1
        l ,r = 0 , len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]== target:
                return m
            if nums[l]<= nums[m]:
                if nums[l] > target or nums[m] < target:
                    l = m+1
                else:
                    r= m-1
            else:
                if nums[r] < target or nums[m] > target:
                    r= m-1 
                else:
                    l =m + 1
        return res