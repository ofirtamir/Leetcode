class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force
        # for i in range(len(nums)):
        #     for x in range (i+1,len(nums)):
        #         if nums[i] + nums[x] == target:
        #             return [i , x]

        dic = {}
        enum =enumerate(nums)
        for i, n in enum :
            diff = target - n
            if diff in dic:
                return [dic[diff], i]
            dic[n] = i
