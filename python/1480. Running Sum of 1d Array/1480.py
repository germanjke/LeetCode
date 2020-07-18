class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            v = sum(nums[:i+1])
            res.append(v)
            
        return res
