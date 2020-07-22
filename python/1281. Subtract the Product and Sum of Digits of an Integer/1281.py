class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n) #to iterate this int we will convert this to string
        product = 1 #product
        summ = 0 #sum 
        for i in s:
            product *= int(i) #so we just multiply each other (start with 1 cause anything * 1 = anything)
            summ += int(i)  #so we just summing each other (start with 0 cause anything + 0 = anything)
        return product - summ #retrun what you need
