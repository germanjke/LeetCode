class Solution {
public:
    int subtractProductAndSum(int n) {
        string s = to_string(n);
        int product,sum;
        product=1;
        sum=0;
        for(int i = 0; i<s.length();i++)
        {
            product*=(s[i]-'0');
            sum+=(s[i]-'0');
        }
        return product-sum;
    }
};
