class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        if strs == []:
            return ans
        for i in range(len(min(strs))):
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return ans
            ans += c
        return ans
    
                    
