class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for a in range(i+1, len(nums)):
        #         if nums[a] == nums[i] :
        #             return True
        # return False
        return len(set(nums)) < len(nums)

