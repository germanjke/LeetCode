class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num) #make num as string
        for i in range(len(s)): #for looping 
            if s[i] == '6': #if s[i] == 6 
                s = s[:i] + '9'+ s[i+1:] #we should exchange it with 9 
                break #while this done we shoud break
        num = int(s) #return it as int
        return num
