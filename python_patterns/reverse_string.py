def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            swap(s, i, n-i-1)
            
Input
["h","e","l","l","o"]
Output
["o","l","l","e","h"]
