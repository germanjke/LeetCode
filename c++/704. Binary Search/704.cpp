class Solution {
public:
    int search(vector<int>& nums, int target) {
        if(nums.size() == 0) //if list empty
            return -1;
        int l = 0; //first element index
        int r = nums.size(); //last element + 1 index
        while (l+1<r){ //while this
            int m = l + (r-l)/2; //we search mid
            if(nums[m]>target){ //if nums[mid] > target
                r=m; //now our mid is right element 
            }else{
                l=m; //else our mid is left element
            }
        }return nums[l]==target?l:-1; //and if this single elemnt == target we return this index
    }
};
