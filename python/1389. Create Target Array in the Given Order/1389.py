class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = [] #init empty list
        for i in range(len(nums)): #iterating in range of len nums
            target.insert(index[i],nums[i]) #now we gonna insert index[i] to index of target, and nums[i] to value
        return target 
