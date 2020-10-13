class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    pairs.append([i,j])
        return len(pairs)
