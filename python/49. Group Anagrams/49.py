class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictx = {}
        for w in strs:
            key = tuple(sorted(w)) #sorting every word
            dictx[key] = dictx.get(key, []) + [w] #adding empty list and adding w in this empty list
        return dictx.values()
