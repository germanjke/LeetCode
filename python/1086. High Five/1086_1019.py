class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students = {}
        res = []
        
        for i in items:
            if i[0] not in students.keys():
                students[i[0]] = [i[1]]
            else:
                students[i[0]].append(i[1])
        
        for k,v in students.items():
            v = sorted(v)
            
            v = v[len(v)-5:len(v)]
            
            students[k] = int(sum(v)/5)
            res.append([k, students[k]])
            
        return res
