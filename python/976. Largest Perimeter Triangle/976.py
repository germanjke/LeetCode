class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
    	L, _ = len(A), A.sort() #sort our array
    	for i in range(L-1,0,-1): #from last to first in sorted array
    		if A[i] < A[i-1] + A[i-2]: return sum(A[i-2:i+1])
    	return 0
    
#чекаем тройки. (i, i+1, i+2) (они идут в обратном порядке в нашем list A)
#если первый элемент с конца меньше двух следующих элементов, то возвращаем сумму от этих трёх элементов, иначе смотрим на некст тройку

#cheking triples (i, i+1, i+2) (reversed sort in array A)
#if first element from end < both next elements, then return sum of this triple, else going next triple
		
