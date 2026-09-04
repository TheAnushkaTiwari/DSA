class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        largest=0
        minimum=0
        n=len(nums)
        for i in range(0,n):
            prefix_array=nums[:i+1]
            suffix_array=nums[i:]
            largest=max(prefix_array)
            minimum=min(suffix_array)
            if largest-minimum<=k:
                return i
        return -1
