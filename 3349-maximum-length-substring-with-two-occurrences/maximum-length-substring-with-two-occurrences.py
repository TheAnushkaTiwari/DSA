class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        char_count = {}
        
        # 'right' expands our window one character at a time
        for right in range(len(s)):
            char = s[right]
            # Add the new character to our hash map
            char_count[char] = char_count.get(char, 0) + 1
            
            # If the current character appears more than twice, 
            # our window is invalid. We must shrink it from the left.
            while char_count[char] > 2:
                # Remove the leftmost character from our count
                char_count[s[left]] -= 1
                # Slide the left edge of the window forward
                left += 1
                
            # Now the window is guaranteed to be valid. 
            # Update our record if this window is the biggest one yet!
            window_size = right - left + 1
            max_len = max(max_len, window_size)
            
        return max_len