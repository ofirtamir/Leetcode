class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # while len(stones)>1:
        #     y= max(stones)
        #     stones.remove(y)
        #     x= max(stones)
        #     stones.remove(x)
        #     if y>x:
        #         stones.append(y-x)
        #     elif x== y:
        #         continue
        # if len(stones)==0:
        #     return 0
        # return stones[0]
        
        max_heap =[-n for n in stones]
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            y= heapq.heappop(max_heap)
            x= heapq.heappop(max_heap)
            if y<x:
                    heapq.heappush(max_heap,y-x)
            elif x==y:
                continue
        if len(max_heap)==0:
            return 0
        return -max_heap.pop()


        