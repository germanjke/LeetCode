class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        # [1,1,0]        [1,0,0]
        # [1,0,1]   ->   [0,1,0]
        # [0,0,0]        [1,1,1]
        
        for row_i in range(len(A)):
            A[row_i] = A[row_i][::-1]
        
        for row_i in range(len(A)):
            for i in range(len(A[row_i])):
                if A[row_i][i] == 0:
                    A[row_i][i] = 1
                else:
                    A[row_i][i] = 0
        return A
