class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max =0
        # for i, a in enumerate(height):
        #     for x, b in enumerate(height):
        #         if i==x:
        #             continue
        #         if a > b :
        #             sam = abs(i-x) * b
        #             if sam >max:
        #                 max =sam
        #         else:
        #             sam = abs(i-x ) * a
        #             if sam > max:
        #                 max = sam
        # return max
        #####
        # res =0
        # for i in range(len(height)):
        #     for x in range(i+1, len(height)):
        #         era = (x-i) * min(height[i],height[x])
        #         res= max(era, res)
        # return res
        #####
        res = 0
        l =0
        r = len(height)-1
        while l < r:
            era = (r-l) * min(height[l], height[r])
            res = max(era, res)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1 
        return res