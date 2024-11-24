class Solution:
    def hammingWeight(self, n: int) -> int:
        c =bin(n)[2:]
        x=Counter(c)
        return x["1"]