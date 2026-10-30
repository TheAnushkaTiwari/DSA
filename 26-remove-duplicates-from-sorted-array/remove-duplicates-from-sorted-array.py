class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        left=0
        for right in range(len(nums)):
            if nums[left]!=nums[right]:
                left+=1
                nums[left]=nums[right]
        return left+1
        
        