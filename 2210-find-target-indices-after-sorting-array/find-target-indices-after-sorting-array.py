class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        result=[]
        n=len(nums)
        for _ in range(n-1):
            for i in range(n-1):
                if nums[i]>nums[i+1]:
                    nums[i], nums[i+1]= nums[i+1], nums[i]
        for j in range(n):
            if nums[j]==target:
                result.append(j)
        return result