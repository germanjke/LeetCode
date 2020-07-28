class Solution {
    public int search(int[] nums, int target) {
        if(nums.length == 0) // if len length = 0 we dont need to check this 
            return -1; 
        int l = 0; // first element of list
        int r = nums.length; // last + 1 element of list
        while(l+1<r){ // while l+1<r we should check. cause if its last two elements we dont need to check mid
            int m = l + (r-l)/2; // so mid 
            if(nums[m]>target){ // if nums [mid] > target we redefine r as m
                r=m;
            }else{ // else l as m
                l=m;}
        }
        if(nums[l] == target){ // so if our nums [left] == target we should return this index
            return l;
        }else{ // else -1 
            return -1;
        }
    }
        
}
