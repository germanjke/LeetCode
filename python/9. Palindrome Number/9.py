class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        reversed_strx = strx[::-1]
        if strx == reversed_strx:
            return True
        else:
            return False
