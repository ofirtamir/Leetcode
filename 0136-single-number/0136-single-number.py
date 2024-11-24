class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # x =Counter(nums)
        # return x.most_common()[-1][0]
        res= 0
        for n in nums:
            res = n ^ res
        return res
        