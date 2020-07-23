class Solution {
public:
    int balancedStringSplit(string s) { 
        int balanced=0,count=0; //define 2 new ints
        for (int i=0;i<s.size();i++){ //for looping into s.size
            if (s[i] == 'R') //count Rs and Ls
                balanced+=1; //if its R we goin +1 to balanced
            if (s[i] == 'L') 
                balanced-=1; //else -1
            if (balanced == 0)
                count+=1; //and if we get balanced if 0 we should add 1 to our result counter
        }
        return count;
    }
};
