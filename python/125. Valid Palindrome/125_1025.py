class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ''
        s = s.lower()
        all_chars = list(map(chr, range(97, 123)))
        all_nums = [str(x) for x in range(10)]
        for char in s:
            if char in all_chars or char in all_nums:
                ans += char
                
        print(ans)
        
        if len(ans) == 0:
            return True
        
        return ans == ans[::-1]
