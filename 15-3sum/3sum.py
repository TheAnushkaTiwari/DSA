class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 1. Sort the array to easily manage duplicates and use two pointers
        nums.sort()
        triplets = []
        
        # 2. Loop through the array, fixing one number at a time
        for i in range(len(nums) - 2):
            # Skip duplicate values for our fixed first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 3. Setup two pointers for the remaining section of the array
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    # Sum is too small, move the left pointer to a bigger number
                    left += 1
                elif total > 0:
                    # Sum is too big, move the right pointer to a smaller number
                    right -= 1
                else:
                    # We found a valid triplet!
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    # 4. Skip duplicates for the second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # 5. Move both pointers inward to keep searching for MORE pairs
                    left += 1
                    right -= 1
                    
        return triplets
        