def search_position(nums,target):
    hi,lo= len(nums)-1, 0
    while lo<=hi:
        mid=(lo+hi)//2
        if target==nums[mid]:
            return mid
        elif target>nums[mid]:
            lo=mid+1
        else:
            hi=mid-1
    return lo
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return search_position(nums,target)
        