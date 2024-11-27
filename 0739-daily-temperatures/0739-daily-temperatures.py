class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # size= len(temperatures)
        # res = [0]* size
        # count=1
        # m =max(temperatures)
        # for i in range(size):
        #     count=1
        #     if temperatures[i]>= m:
        #         continue
        #     for x in range(i+1 , size):
        #         if temperatures[i] < temperatures[x]:
        #             res[i] = count
        #             break
        #         count +=1
        
        stack =[]
        res= [0]*len(temperatures)
        for i , t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                num , inx = stack.pop()
                res[inx]= i - inx
            stack.append([t, i])
        return res
                
        return res