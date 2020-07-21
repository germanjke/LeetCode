class Solution{
public:
    int xorOperation(int n, int start){
        int x = 0; //here will be next result
        vector<int>v; //new vector of ints
        for (int i=0;i<n;i++) //for looping in len of array (n)
        {
            v.push_back(start+2*i); //adding our formula to each index
        }
        for (int i=0;i<v.size();i++) //for looping in vector v
            x=x^v[i]; //and doing XOR
        return x;
    }
};
