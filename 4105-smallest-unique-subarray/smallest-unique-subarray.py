from collections import defaultdict
from typing import List
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        def check(length: int) -> bool:
           
            prime1, prime2 = 31, 37
            mod1, mod2 = 10**9 + 7, 10**9 + 9
            
            hash1, hash2 = 0, 0
            power1, power2 = 1, 1
            
           
            for _ in range(length - 1):
                power1 = (power1 * prime1) % mod1
                power2 = (power2 * prime2) % mod2
                
            
            for i in range(length):
                hash1 = ((hash1 * prime1) % mod1 + nums[i]) % mod1
                hash2 = ((hash2 * prime2) % mod2 + nums[i]) % mod2
                
            hm = defaultdict(int)
            hm[(hash1, hash2)] += 1
           
            for i in range(length, n):
                out1 = (nums[i - length] * power1) % mod1
                hash1 = (hash1 - out1 + mod1) % mod1
                hash1 = ((hash1 * prime1) % mod1 + nums[i]) % mod1
                
               
                out2 = (nums[i - length] * power2) % mod2
                hash2 = (hash2 - out2 + mod2) % mod2
                hash2 = ((hash2 * prime2) % mod2 + nums[i]) % mod2
                
               
                hm[(hash1, hash2)] += 1
                
           
            for count in hm.values():
                if count == 1:
                    return False
                    
            return True 

        low, high, ans = 1, n, n
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if not check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
        