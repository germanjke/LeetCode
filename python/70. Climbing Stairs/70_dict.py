class Solution:
    def __init__(self):
        self.dic = {1:1, 2:2} #init first two values like Fiba
    
    def climbStairs(self, n):
        if n not in self.dic: #and now we gonna checking dic, so this is Fiba haha
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2) #now we can make n=3 easy. later we can do n=4 etc
        return self.dic[n] #take last
