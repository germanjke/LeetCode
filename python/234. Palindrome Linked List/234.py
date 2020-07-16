# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool: 
        rev = None #main idea about we gona make new var 'reversed'
        slow = fast = head #ok lets define our slow and fast
        
        while fast and fast.next: #while we have next
            fast = fast.next.next #faster have x2 speed
            rev, rev.next, slow = slow, rev, slow.next #rev = slow, and rev going in reverse side and slow to right side
            
        if fast: #if all is ok 
            slow = slow.next #we gonna make move slow to but with x1 speed
            
        while rev and rev.val == slow.val: #while we have reverse and rev val = slow val 
            slow = slow.next #goin check all of slow and rev val values with next operator
            rev = rev.next
        return not rev #so if all values is ok and our while not ending we can sayits not more elements later and all of them equal so return not rev (True)
