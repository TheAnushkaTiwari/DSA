class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_string=str(x)
        reverse_num=num_string[::-1]
        if reverse_num==num_string:
            return True
        else:
            return False