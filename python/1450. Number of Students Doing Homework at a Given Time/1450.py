class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            a = [x for x in range(startTime[i],endTime[i]+1)]
            if queryTime in a:
                count += 1
        return count
