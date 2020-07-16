# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == 0: return False
            
        current = head #мы тут  
        steps = 1 #шажочек сначала 1
        
        while True: 
            next_node = current #начинаем тут
            for step in range(steps): #и потихоньку идём
                if next_node == None: #если в конце будет нулик нам такое не нужно
                    return False
                
                next_node = next_node.next # а теперь разберем настоящий мужской случай
                if next_node == current: #вот она!!! мы её нашли)
                    return True 
                    
            current = next_node #ну и делаем переназначение нашей каррент ноды
            
            steps *= 2 #шажочек в два раза увеличиваем и поехали
            
#this is solving by moscow math school 
#московская школа сильна
