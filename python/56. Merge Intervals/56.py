class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        if len(intervals) == 0:
            return []
        
        res = []
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            a = res[-1]
            b = intervals[i]
            #we will equal a and b (first and iter element)
            if b[0] > a[-1]: #we dont need a then
                res.append(b) 
            else:
                res[-1][-1] = max(a[-1],b[-1])
                
        return res
