class Solution:
    def countBits(self, n: int) -> List[int]:
        res =[0]*(n+1)
        for i in range(len(res)):
            res[i]=Counter(bin(i)[2:])["1"]
        return res
        