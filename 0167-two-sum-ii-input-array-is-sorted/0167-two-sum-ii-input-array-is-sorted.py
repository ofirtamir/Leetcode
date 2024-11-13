class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for x in range(i+1 ,len(numbers)):
        #         if target- numbers[i] > numbers[x]:
        #             continue
        #         if numbers[i] + numbers[x] == target:
        #             return [i+1,x+1]                    
        s = 0
        e = len(numbers) - 1
        while(numbers[s]+ numbers[e] != target):
            if numbers[s] + numbers[e] > target:
                e = e-1
            elif numbers[s] + numbers[e] < target:
                s = s + 1
        
        return [s +1 ,e + 1]
