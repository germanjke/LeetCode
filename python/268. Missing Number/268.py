class Solution(object):
    def missingNumber(self, nums):
        return sum(range(len(nums)+1)) - sum(nums) 

#we have list of n digists from 0 to n and one this is missing
#if we will take sum of indexes and get +1 to this we will take sum of array with this mssing value
#so next step we need to delete sum of given nums to get only missing value
