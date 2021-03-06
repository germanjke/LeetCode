class Solution:
    def bitwise(self,arr): # Function for determine result of XOR
        XOR = arr[0]
        for i in range(1,len(arr)):
            XOR = XOR^arr[i] #we need to know what is XOR
        return XOR
    def xorOperation(self, n: int, start: int) -> int:
        nums = [0 for x in range(n)] #first we give nums of all zeros
        for i in range(n): #and later for all indexes we will fill values 
            nums[i] = start + 2*i
        return self.bitwise(nums) #then we XORing our nums
