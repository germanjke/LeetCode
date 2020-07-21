class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) { 
        vector<int> res;  //я создаю пустой список для будущего рез-та
        for (int i=0;i<nums.size();i++) //проверяю по индексам из nums
        {
            int count = 0; //завожу переменную которая будет считать сколько элементов больше
            for (auto x : nums) //теперь делаю for loop в самих nums по значениям
            {
                if (nums[i]>x) //если nums с индексом i больше чем значение num из nums
                    count += 1; //увеличим на единичку наш count
            }
            res.push_back(count); //в конце первого лупа мы добавим этот каунт в наш res
            //так и будут добавляться каунты
        }
        return res; //выведем список из всех каунтов
        
    }
};
