class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r ,res =0 ,1 ,0
        while r < len(prices):
            if prices[l] < prices[r]:
                p= prices[r]-prices[l]
                res= max(res,p )
            else:
                l=r
            r+=1
        return res