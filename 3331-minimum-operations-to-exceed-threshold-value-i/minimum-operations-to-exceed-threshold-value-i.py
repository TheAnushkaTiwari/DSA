class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operations=0
        while True:
            smallest_element=min(nums)
            if smallest_element<k:
                nums.remove(smallest_element)
                operations+=1
            else:
                return operations