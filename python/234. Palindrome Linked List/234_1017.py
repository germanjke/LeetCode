# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        
        
        n = len(ans)
        
        if n % 2 == 0:
            return ans[0:n//2] == ans[n//2:][::-1]
        
        else:
            print(ans[0:n//2])
            print(ans[(n//2) + 1:])
            return ans[0:n//2] == ans[(n//2)+1:][::-1]
            
