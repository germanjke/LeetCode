class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
        
        dictionary = dict(zip(alphabet, morse_list))
        
        res = []
        for word in words:
            ans = ''
            for char in word:
                ans += dictionary[char]
            res.append(ans)
        
        return len(set(res))
            
