class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = []
        for i in range(len(nums)):
            for x in range (i+1,len(nums)):
                if nums[i] + nums[x] == target:
                    return [i , x]
