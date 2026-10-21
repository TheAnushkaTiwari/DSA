class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        num=list(nums)
        for i in range(len(num)):
            curr=num.pop(i)
            j=i-1
            while j>=0 and curr%2==0:
                j-=1
            num.insert(j+1, curr)
        return num
        