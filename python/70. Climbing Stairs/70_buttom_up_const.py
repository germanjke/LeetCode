class Solution:
    def climbStairs(self,n):
        #this is bottom-up const space
        if n==1: return 1 # ok
        res = [0] * n #initialization with zeros
        a, b = 1 , 2 
        for i in range(2,n): #go from 3rd element
            tmp = b  #so we need to make tmp (b) = 2
            b = b + a #then we goin to 3rd elemnt so we need +a so b=3 now
            a = tmp #this is for next iter so a is 2 now
        return b
    
    #next iter for 4th element:
    #tmp = b = 3
    #b = b+a, 3+2 = 5 
    #a = 3 now
    #we return 5
    
    #next iter for 5th elemnt:
    #tmp = b = 5 
    #b = b+a , 5+3 = 8 
    #a = 5 now
    #we return 8
    
    #etc
