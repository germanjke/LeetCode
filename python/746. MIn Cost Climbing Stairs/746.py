class Solution:
    def minCostClimbingStairs(self, cost):
        for i in range(2, len(cost)): #from second elemnt cause we know can search first two
            cost[i] += min(cost[i - 1],cost[i - 2]) #so we just need to check min of i-1 and i-2
        return min(cost[-1], cost[-2]) #return minimum of last and prelast in const
