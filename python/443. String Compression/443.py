def split(word): 
    return [char for char in word] 

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if len(chars) == 1:
            return 
        
        res = []
        
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            
            else:
                res.append(chars[i-1])
                if count > 1:
                    res.extend(split(str(count)))
                count = 1
                
        res.append(chars[i])
        if count > 1:
            res.extend(split(str(count)))
        
        
        chars[:] = res[:]  # cause of problem task
       
                
