def numberOfRotations(nums):
    n=len(nums)-1
    lo,hi=0,n
    largest_element=nums[n]
    while lo<hi:
        mid=(lo+hi)//2
        if nums[mid]>largest_element:
            largest_element=nums[mid]
            lo=mid
        elif nums[mid]==largest_element:
            return mid
        else:
            hi=mid
    return n
    

class Solution:
    def findMin(self, nums: List[int]) -> int:
        rotations= numberOfRotations(nums)
        if rotations==len(nums)-1:
            return nums[0]
        else:
            return nums[rotations+1]
       

        