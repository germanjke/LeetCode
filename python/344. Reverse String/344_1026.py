def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            swap(s, i, n-i-1)
