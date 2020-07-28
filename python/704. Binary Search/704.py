class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: #if its empty we dont even need to to check something
            return -1
        l = 0 #lets define left like our first element index
        r = len(nums) #and lets define right our last elemnt + 1 index
        while l+1<r: #so we searching mid when its at least 3 elements in list 
            m = l+(r-l)//2 #search mid
            if nums[m]>target: #if elemnt with m index > target 
                r=m #we should update right
            else: 
                l=m #else - left
        if nums[l] == target: #so if our nums[l] (updated l) we gonna equal with our target
            return l #and if its ok we gonna return this
        else:
            return -1
            
