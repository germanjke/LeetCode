class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        len1 = len(sentence1)
        len2 = len(sentence2)
        if len1 != len2:
            return False
        
        count = 0
        
        for i in range(len1):
            if sentence1[i] == sentence2[i]:
                count += 1
            
            temp = [sentence1[i], sentence2[i]]
            if temp in similarPairs or temp[::-1] in similarPairs:
                count += 1
        
        if count == len1:
            return True
        return False
