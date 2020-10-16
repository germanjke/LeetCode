class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        r = 0
        count = 0
        for char in s:
            if char == 'L':
                l += 1
            if char == 'R':
                r += 1
            if l == r:
                count += 1
                l = 0
                r = 0
        return count
            
            
