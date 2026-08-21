class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # In Python, we can get the max unique letters instantly using a set
        max_unique = len(set(s))
        result = 0
        
        # Run a sliding window for every possible target of unique characters (1 to max_unique)
        for curr_unique in range(1, max_unique + 1):
            count_map = {}
            window_start = 0
            window_end = 0
            unique = 0
            count_at_least_k = 0
            
            while window_end < len(s):
                # Expand the sliding window
                if unique <= curr_unique:
                    char_end = s[window_end]
                    if count_map.get(char_end, 0) == 0:
                        unique += 1
                    
                    count_map[char_end] = count_map.get(char_end, 0) + 1
                    
                    if count_map[char_end] == k:
                        count_at_least_k += 1
                        
                    window_end += 1
                    
                # Shrink the sliding window
                else:
                    char_start = s[window_start]
                    if count_map[char_start] == k:
                        count_at_least_k -= 1
                        
                    count_map[char_start] -= 1
                    
                    if count_map[char_start] == 0:
                        unique -= 1
                        
                    window_start += 1
                    
                # Check if our current window perfectly matches all constraints
                if unique == curr_unique and unique == count_at_least_k:
                    result = max(result, window_end - window_start)
                    
        return result
        
        