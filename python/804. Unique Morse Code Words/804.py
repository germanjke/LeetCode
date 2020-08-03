class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                    'u', 'v', 'w', 'x', 'y', 'z']
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                 ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                 "...","-","..-","...-",".--","-..-","-.--","--.."]
        dictionary = dict(zip(alphabet, morse)) #keys, values
        w = '' #each word we start from zero
        res = [] #each word we will add to res
        for word in words:
            for i in word:
                w+=dictionary[i] #so we building our word from our dict
            res.append(w) 
            w = '' #dont forget restart word 
         
        return len(set(res)) #return number of unique values
