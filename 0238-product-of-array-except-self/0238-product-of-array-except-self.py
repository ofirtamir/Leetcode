class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n =len(nums)
        # pr = [0] * n
        # po = [0] * n
        # res =[0] * n
        # pr[0] =po[n-1]= 1
        # for i in range(1,n):
        #     pr[i]= pr[i-1] * nums[i-1]
        # for x in range (n-2, -1, -1):
        #     po[x] =po[x+1] * nums[x+1]
        
        # for i in range(n):
        #     res[i] = pr[i] * po[i]
        # return res

        n= len(nums)
        res = [1] * n
        pr = 1
        for i in range(n):
            res[i] *= pr
            pr *= nums[i]
        po = 1
        for i in range(n-1,-1,-1):
            res[i] *= po
            po *= nums[i]
        return res
        
        