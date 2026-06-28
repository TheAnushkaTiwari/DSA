class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        #using Boyer-Moore Voting Algorithm as the maajority element will appear more than n/2 times
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate