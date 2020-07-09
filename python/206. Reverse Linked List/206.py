# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
            lst = []
            current = head
            while current:
                lst.append(current.val)
                current = current.next

            lst = lst[::-1]
            # construct a link list from the tail
            nxt = None
            while lst:
                val = lst.pop()
                node = ListNode(val)
                node.next = nxt
                nxt = node

            return(nxt)
