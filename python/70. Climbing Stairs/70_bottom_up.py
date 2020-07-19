class Solution:
    def climbStairs(self,n):
        #this is bottom-up with O(n)
        if n==1: return 1 # ok
        res = [0] * n #initialization with zeros
        res[0], res[1] = 1, 2 #like fiba
        for i in range(2,n): #now we go from 2
            res[i] = res[i-1] + res[i-2] #now we can make this for 3, next we go to 4 etc
        return res[-1] #last
        
