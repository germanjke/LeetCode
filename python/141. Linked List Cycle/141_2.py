# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None: return None # тут понятно думаю
        
        slow, fast = head, head.next # фастевич будет в два раза быстрее
        
        while fast and fast.next: # пока есть фаст и фаст некст (короче нуль обходим)
            if slow.val == fast.val: # если попали то возвраащем тру
                return True
            
            slow = slow.next #увеличиваем в раз
            fast = fast.next.next #увеличиваем в два раза
            
        return False
        
#так во всем мире решают
