class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        ind = {}
        ans = []
        
        for i in range(len(B)):
            ind[B[i]] = i
        
        for n in A:
            if n in ind.keys():
                ans.append(ind[n])
        
        return ans
