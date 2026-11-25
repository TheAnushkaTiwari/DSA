import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n=len(nums)
        max_len=0
        for i in range(n):
            curr_gcd=0
            curr_lcm=1
            prod=1
            for j in range(i,n):
                num=nums[j]
                prod=prod*num
                curr_gcd=math.gcd(curr_gcd,num)
                curr_lcm=math.lcm(curr_lcm,num)
                if prod==curr_gcd*curr_lcm:
                    max_len=max(max_len,j-i+1)
        return max_len