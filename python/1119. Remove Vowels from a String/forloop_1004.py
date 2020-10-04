class Solution:
    def removeVowels(self, S: str) -> str:
        ans = ''
        for char in S:
            if char not in ['a','e','i','o','u']:
                ans += char
        return ans
