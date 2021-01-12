class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if len(nums) == 0:
            return []
        
        if len(nums) == 1:
            return [str(nums[0])]
        
        res = []
        start = nums[0]
        count = 0
        
        for i in range(1, len(nums)):
            
            if start + count + 1 == nums[i]:
                
                count += 1
                
            else:
                if count > 0:
                    
                    res.append(str(start) + '->' +str(start + count))

                    start = nums[i]
                    count = 0
                
                else:
                    
                    res.append(str(start))
                    start = nums[i]
                    
        if count > 0:
            res.append(str(start) + '->' + str(start + count))
            
        else:
            res.append(str(start))

            
        return res
