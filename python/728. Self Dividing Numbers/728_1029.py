class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lis = []
        for num in range(left, right+1):
            if self.isGoodNumber(num) == True:
                lis.append(num)
        return lis
        
        
    def isGoodNumber(self, num: int) -> bool:
        x = num
        while x > 0:
            rem = x % 10
            if rem !=0  and num % rem == 0:
            
                x = x // 10
            else:
                return False
        return True
    
        
        
