class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int count = 0, i,j;
        for (i=0;i<=nums.size()-1;i++){
            for (j=0;j<=nums.size()-1;j++){
                if (nums[i] == nums[j] && i < j){
                    count += 1;
                }
            }
        }
        return count;
    }
};
