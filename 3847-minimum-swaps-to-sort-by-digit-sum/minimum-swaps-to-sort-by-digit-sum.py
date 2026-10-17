class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digitSum(n):
            sum=0
            while n>0:
                sum+=n%10
                n=n//10
            return sum
        n = len(nums)
        target = sorted(nums, key=lambda x: (digitSum(x), x))
        
        # Step 2: Map each value to its correct index in the sorted array
        pos_map = {val: i for i, val in enumerate(target)}
        
        vis = [False] * n
        cycles = 0
        
        # Step 3: Count permutation cycles
        for i in range(n):
            if not vis[i]:
                curr = i
                while not vis[curr]:
                    vis[curr] = True
                    val = nums[curr]
                    curr = pos_map[val]
                cycles += 1
                
        # Total elements minus number of cycles gives minimum swaps
        return n - cycles



        