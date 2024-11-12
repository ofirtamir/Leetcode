class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dic =Counter(nums)
        # sort = sorted(dic.items(), key = lambda x :x[1], reverse= True)
        # res =[]
        # for i in range(k):
        #     res.append(sort[i][0])

        # return res

        dic = Counter(nums)
        fr =[[] for i in range(len(nums) + 1)]
        for n ,c in dic.items():
            fr[c].append(n)
        
        res= []
        for i in range(len(nums),0,-1):
            for n in fr[i]:
                res.append(n)
                if len(res)== k:
                    return res