class Solution:
    def myPow(self, x: float, n: int) -> float:
        # res=1
        # if n==1:
        #     return x
        # if n==0:
        #     return 1
        # if n>1:
        #     for i in range(n):
        #         res= res*x
        # if n<0:
        #     for i in range(0,n,-1):
        #         res= res/x
        # return res
        def helper(x,n):
            if x== 0:
                return 0
            if n==0: return 1

            res= helper(x*x,n//2)
            return x * res if n%2==1 else res
        return helper(x,abs(n)) if n>0 else 1/ helper(x,abs(n))