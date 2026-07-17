class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        lo,hi=1,1
        for i in range(2,n+1):
            current= lo+hi
            lo=hi
            hi=current
        return hi
        