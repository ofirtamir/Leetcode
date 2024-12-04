class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        res=[]
        for inter in intervals:
            if not res or inter[0]> res[-1][1]:
                res.append(inter)
            else:
                res[-1][1]= max(res[-1][1],inter[1])
        return res