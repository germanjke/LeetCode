class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dictionary = {v:i for i,v in enumerate(keyboard)}

        ans = 0
        curr = 0
        
        for char_index in range(len(word)):
            ans += abs(dictionary[word[char_index]] - curr)
            print(dictionary[word[char_index]])
            curr = dictionary[word[char_index]]   
            
        return ans
