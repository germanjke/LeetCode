# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # for x in range(1, n+1):
        #     if isBadVersion(x) == True:
        #         return x       
        
        l = 1
        r = n
        
        while l<=r:
            mid = l + (r-l)//2
            if isBadVersion(mid) == True and isBadVersion(mid-1) == False:
                return mid
            if isBadVersion(mid) == True:
                r = mid - 1
            if isBadVersion(mid) == False:
                l = mid + 1
