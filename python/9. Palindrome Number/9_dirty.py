class Solution:
    def isPalindrome(self, x: int) -> bool:
        #search the median
        s = str(x)
        if len(s) == 2:
            if s[0] == s[1]:
                return True
            else:
                return False
        if len(s)%2 == 1:
            median = int(len(s)//2) 
            if s[0:median] == s[:median:-1]:
                return True 
            else:
                return False
        if len(s)%2 == 0:
            median = int(len(s)/2)
            if s[0:median] == s[:median-1:-1]:
                return True 
            else:
                return False
                
  #yes its dirty but its works lol
