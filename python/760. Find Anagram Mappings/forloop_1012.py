class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        dictionary = {v:i for i,v in enumerate(B)}
        for x in A:
            res.append(dictionary[x])
        return res
