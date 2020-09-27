class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(numbers):
            m = target - n
            if m in d:
                return [d[m] + 1, i+1]
            else:
                d[n] = i
                
          
