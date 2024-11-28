class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        item = self.dic[key]
        l, r = 0 , len(item)-1
        m=0
        while l <= r:
            m = (r+l)//2
            if item[m][1] == timestamp:
                return item[m][0]
            if item[m][1] > timestamp:
                r= m-1
            else:
                l= m+1
        return item[r][0] if r>=0 else ""
                

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)