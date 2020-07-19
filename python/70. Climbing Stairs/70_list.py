class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        dic = [-1 for i in range(n)] #memo list
        dic[0],dic[1] = 1,2 #we know first two events
        return self.helper(n-1, dic)
    
    def helper(self,n,dic):
        if dic[n]<0: #it's always cause we do memo with -1
            dic[n] = self.helper(n-1,dic) + self.helper(n-2,dic) #fiba  
        return dic[n] #return last
