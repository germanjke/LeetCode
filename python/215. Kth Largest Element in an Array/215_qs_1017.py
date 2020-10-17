def quicksort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    less = [x for x in nums[1:] if x <= pivot]
    greater = [x for x in nums[1:] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return quicksort(nums)[-k]
        
