class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count=0
        for i in range(100,1000,2):
            temp=i
            num1=temp//100
            num2=((temp//10)%10)
            num3=temp%10
            candidate_digits=[num1,num2,num3]
            if all(digits.count(d) >= candidate_digits.count(d) for d in set(candidate_digits)):
                count += 1
        return count
            
        