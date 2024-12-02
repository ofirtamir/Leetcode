class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # h= []
        # heap.heapipy(h)
        # for x,y in points:
        #     heap.heapposh(h, (x**2 +y**2)**0.5)
        h= [(x[0]**2 +x[1]**2)**0.5 for x in points]
        res =[]
        for i in range(k):
            x= min(h)
            inx= h.index(x)
            res.append(points[inx])
            h.remove(x)
            points.pop(inx)
        return res
        