#without using string and with minimumspace complexity
'''def is_pallindrome(x):
    if x<0 or (x%10==0 and x!=0):
        return False
    head,tail=x,0
    while head>tail:
        tail= tail*10 + head%10
        head= head//10
    return head==tail or head==(tail//10)
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_string=str(x)
        reverse_num=num_string[::-1]
        if reverse_num==num_string:
            return True
        else:
            return False