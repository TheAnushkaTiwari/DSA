def max_count_of_target_string(s: str, target: str) -> int:
    unique_target_chars = set(target)
    min_copies = float('inf')
    for char in unique_target_chars:
        available = s.count(char)
        needed = target.count(char)
        possible_copies = available // needed
        if possible_copies < min_copies:
            min_copies = possible_copies
            
    return min_copies

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        return max_count_of_target_string(s, target)