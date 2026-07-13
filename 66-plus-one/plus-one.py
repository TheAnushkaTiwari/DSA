class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)-1
        add=1
        num=0
        if digits[n]+1>9:
            for i in digits[::-1]:
                num+=i*add
                add*=10
            num+=1
            num_str=str(num)
            digits=[int(x) for x in num_str]
        else:
            digits[n]=digits[n]+1
        return digits
        