class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0 
        for i in nums:
            s = str(i) #we will just count len of string 
            if len(s)%2 == 0: #so if its even we gonna make count +1 
                count +=1
        return count
