class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = curr = 0
        for num in nums:
            prev, curr = curr, max(num + prev , curr)
        return curr
        
        
        
        
        
        
#ok lets have some example [2,7,9,3,1]
#1st iteration (nums[0]=2), prev = 0, curr = max(2+0, 0) = 2, so now prev = 0, curr = 2
#2st iteration (nums[1]=7), prev = 2, curr = max(7+2, 2) = 9, so now prev = 2, curr = 9
#3st iteration (nums[2]=9), prev = 9, curr = max(9+2, 9) = 11, so now prev = 9, curr = 11
#4st iteration (nums[3]=3), prev = 11, curr = max(3+9, 11) = 12, so now prev = 11, curr = 12
#5st iteration (nums[4]=1), prev = 12, curr = max(1+9, 12) = 12, so now prev = 12, curr = 12
