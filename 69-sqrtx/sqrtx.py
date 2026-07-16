class Solution:
    def mySqrt(self, x: int) -> int:
        lo,hi=1, x
        if x==0:
            return 0
        while lo<=hi:
            mid=(lo+hi)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                lo=mid+1
            else:
                hi=mid-1
        return hi

        