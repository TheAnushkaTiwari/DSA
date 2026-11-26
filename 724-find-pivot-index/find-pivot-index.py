class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n=len(nums)
        left=0
        left_sum=0
        total_sum=0
        for num in nums:
            total_sum+=num
        for i in range(n):
            if total_sum-left_sum-nums[i]==left_sum:
                return i
            left_sum+=nums[left]
            left+=1
        return -1
            
            
        