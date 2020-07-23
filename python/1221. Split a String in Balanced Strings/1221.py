class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = {'R' : 0, 'L' : 0} #we will be count how much Ls and Rs in string
        res = 0 #if count of Rs and Ls are equal we need to +1 to res
        for i in s:
            if i == 'R':
                count['R'] += 1
            elif i == 'L':
                count['L'] += 1
            if count['R'] == count['L']:
                res += 1
        return res
