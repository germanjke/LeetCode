class Solution:
    def reverseWords(self, s: str) -> str:
        s = reversed(s.split()) #just splitting our s and make list with reverse
        res = ' '.join(s) #joining all of thiswith space
        return res
