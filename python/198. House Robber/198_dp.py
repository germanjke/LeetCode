class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prev = curr = 0 #here we go lets begin with 0 and will up this per for loop hehe 
        for num in nums: #ok let's check all of our nums
          temp = prev # This represents the nums[i-2]th value 
          prev = curr # This represents the nums[i-1]th value
          curr = max(num + temp, prev) # Here we just plug into the formula
        return curr
