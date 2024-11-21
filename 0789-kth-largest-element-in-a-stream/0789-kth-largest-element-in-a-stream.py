class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kk = k
        if nums ==None:
            self.num=[]
        self.num = sorted(nums) if nums else []

        

    def add(self, val: int) -> int:
        insert= False
        for i in range(0, len(self.num)):
            if self.num[i] >= val:
                self.num.insert(i, val)
                insert= True
                break
        if not insert:
            self.num.append(val)
        return self.num[-self.kk]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)