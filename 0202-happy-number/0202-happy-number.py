class Solution:
    def isHappyy(self, n: int ,s) -> bool:
        if n == 1:
            return True
        s.add(n)

        ex = 0
        while n > 0:
            ex += (n % 10) ** 2
            n //= 10
        if ex in s:
            return False
        return self.isHappyy(ex, s)
    def isHappy(self, n: int) -> bool:
        s =set()
        return self.isHappyy(n ,s)