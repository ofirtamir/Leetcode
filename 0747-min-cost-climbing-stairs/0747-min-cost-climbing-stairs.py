class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # m= 10000
        # def dfs(cost,s, i):
        #     nonlocal m
        #     if i>= len(cost):
        #         m= min(m,s)
        #         return 
        #     dfs(cost,s+cost[i],i+1)
        #     dfs(cost,s+cost[i],i+2)
        # dfs(cost,0,0)
        # dfs(cost,0,1)
        # return m

        # def dfs(cost, i, s):
        #     if i>= len(cost):
        #         return s
        #     return min(dfs(cost, i+1,s+cost[i] ),dfs(cost, i+2, s+ cost[i]))
        # return min(dfs(cost,0,0), dfs(cost,1,0))

        cost.append(0)
        for i in range(len(cost)-3,-1,-1):
            cost[i]+= min(cost[i+1],cost[i+2])
        return min(cost[0], cost[1])

