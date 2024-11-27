class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # mi = min(piles)
        # ma= max( piles)
        # count =0
        # for i in range(1,ma+1):
        #     count =0
        #     cPiles =piles.copy()
        #     while max(cPiles)>0:
        #         for x in range(len(cPiles)):
        #             if cPiles[x]<= 0:
        #                 continue
        #             cPiles[x]-=i
        #             count+=1
        #             if count >h :
        #                 break
        #         if count > h :
        #             break
        #     if count<= h:
        #         return i
        
        l ,r = 1, max(piles)
        res= r
        while l<= r:
            m = (l+r)//2
            hours = 0
            for i in piles:
                hours+= math.ceil(i/m)
            if hours <= h:
                res= min(res,m)
                r= m-1
            else:
                l = m+1
        return res

            



        