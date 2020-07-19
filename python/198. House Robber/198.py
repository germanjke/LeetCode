class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) #len of list
        
        #if we have empty list we have no choice to do something so just return 0
        if n == 0:
            return 0
        
        #if we have only one house we gonna take this
        if n == 1:
            return nums[0]
        
        #if we have two houses we should take maximum value so this is clear i guess
        if n == 2:
            return max(nums[0],nums[1])
        
        #ok now we gonna to make DP cause we have all simple events above
        
        #first of all we need to make big list where we can do some creative art
        
        dp = [0] * len(nums) #and make this list zerolist
        
        dp[0] = nums[0] #first element should be like our event above (with len=1)
        
        dp[1] = max(nums[0],nums[1]) #second should be like our event above( with len=2)
        
        for i in range(2, len(nums)): #we gonna from 3rd element! yes 2 == its 3rd elemnt and going to all of list but w/o last
        
            dp[i] = max(dp[i-1],dp[i-2]+nums[i]) #here is key point
                                                 #we gonna get maximum of i-1 and i-2 with value of num in this i
        
        return dp[-1] #and return last
        
        
