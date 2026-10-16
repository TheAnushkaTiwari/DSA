class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        sum=0
        for i in range(n):
            for j in range(i+1,n+1):
                subarr=nums[i:j]
                k=len(set(subarr))
                sum+=k*k
        return sum


        