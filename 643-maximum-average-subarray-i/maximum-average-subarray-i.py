class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=0
        max_sum=0
        n=len(nums)
        for i in range(0,k):
            window_sum+=nums[i]
        max_sum=window_sum
        for i in range(k,n):
            window_sum-=nums[i-k]
            window_sum+=nums[i]
            max_sum=max(max_sum,window_sum)
        return max_sum/k
        