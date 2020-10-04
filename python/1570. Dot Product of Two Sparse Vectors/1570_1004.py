class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = {i:v for i,v in enumerate(nums) if v}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        a,b = self, vec
        res = 0
        if len(a.d) > len(b.d):
            a,b = b,a 
        for i in a.d:
            if i in b.d:
                res += a.d[i] * b.d[i]
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
