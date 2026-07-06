def largestElement(nums):
    n=len(nums)-1
    lo,hi=0,n
    largest_element=nums[n]
    while lo<hi:
        mid= (lo+hi)//2
        if largest_element<nums[mid]:
            largest_element=nums[mid]
            lo=mid
        elif largest_element==nums[mid]:
            return mid
        else:
            hi=mid
    return lo

def binarySearch(lo, hi,target,nums):
    while lo<=hi:
        mid= (lo+hi)//2
        if target==nums[mid]:
            return mid
        elif target>nums[mid]:
            lo=mid+1
        else: 
            hi=mid-1
    return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if nums[0]<=nums[n-1]:
            return binarySearch(0,n-1,target,nums)
        else:
            largest_element_idx= largestElement(nums)
            if target>=nums[0]:
                return binarySearch(0, largest_element_idx, target, nums)
            else:
                return binarySearch(largest_element_idx+1,n-1,target,nums)
