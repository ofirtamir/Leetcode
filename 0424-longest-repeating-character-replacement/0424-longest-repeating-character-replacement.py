class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # res =0
        # c= k
        # for l in range(len(s)):
        #     for r in range(l,len(s)):
        #         if s[l]==s[r]:
        #             res = max(res, r-l+1)
        #         elif c > 0:
        #              res = max(res, r-l+1)
        #              c-=1
        #         else:
        #             c=k
        #             break
        # return res
        dic =defaultdict(int)
        l ,r = 0 ,0
        res= 0
        while r < len(s):
            dic[s[r]] += 1
            if r -l+1 - max(dic.values()) <= k:
                res= max(res,r -l+1)
            else:
                dic[s[l]]-=1
                l+=1
            r+=1
        return res


                
