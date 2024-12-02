class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones)>1:
            y= max(stones)
            stones.remove(y)
            x= max(stones)
            stones.remove(x)
            if y>x:
                stones.append(y-x)
            elif x== y:
                continue
        if len(stones)==0:
            return 0
        return stones[0]

        