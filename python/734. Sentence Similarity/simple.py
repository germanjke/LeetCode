class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        if sentence1 == sentence2:
            return True
        for i in range(len(sentence1)):
            if ([sentence1[i], sentence2[i]] in similarPairs 
                or [sentence2[i], sentence1[i]] in similarPairs) == False and sentence1[i] != sentence2[i]:
                return False
        return True
