class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [] #making new result list
        for i in range(len(nums)): #and now go for loop in nums (checking by index)
            count = 0 #lets count how much counts we will have
            for num in nums: #now we will for looping in nums (checking by value)
                if nums[i] > num: #here is condition 
                    count+=1 #if its is we +=1 count
            res.append(count) #and add count for single index
        return res #return final list
