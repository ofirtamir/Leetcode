class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # self.kk = k
        # if nums ==None:
        #     self.num=[]
        # self.num = sorted(nums) if nums else []
        self.heap, self.k = nums,k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # insert= False
        # for i in range(0, len(self.num)):
        #     if self.num[i] >= val:
        #         self.num.insert(i, val)
        #         insert= True
        #         break
        # if not insert:
        #     self.num.append(val)
        # return self.num[-self.kk]
        heapq.heappush(self.heap,val)
        if len(self.heap)> self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)