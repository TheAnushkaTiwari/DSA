#instead of this use math library
'''def iscoprime(x,y):
    d=2
    while d<=x and d<=y:
        if x%d==0 and y%d==0:
            return False
        else:
            d+=1
    return True
'''
import math

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n=len(nums)
        beautiful_pairs=0
        for i in range(0,n):
            for j in range(i+1,n):
                str_num1=str(nums[i])
                num1=int(str_num1[0])
                num2=nums[j]%10
                if math.gcd(num1,num2)==1:
                    beautiful_pairs+=1
        return beautiful_pairs
        