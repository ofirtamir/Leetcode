class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic =Counter(nums)
        sort = sorted(dic.items(), key = lambda x :x[1], reverse= True)
        res =[]
        for i in range(k):
            res.append(sort[i][0])

        return res