class Solution:
    def subtractProductAndSum(self, n: int) -> int:
#         s = str(n)
#         product = 1
#         summ = 0
#         for i in s:
#             k = int(i)
#             product *= k
#             summ += k
        
#         return (product - summ)
        
        product = 1
        summ = 0
        while n >= 1:
            k = n%10
            n //= 10
            product *= k
            summ += k
            
        return (product - summ)
