class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num_string=str(n)
        x=""
        total=0
        for digit in num_string:
            if digit != '0':    
                x+=digit
                total+=int(digit)
        if x=="":
            return 0
        return int(x)*total
            