class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result=[]
        for i in range(100,1000,2):
            temp=i
            num1=temp//100
            num2=((temp//10)%10)
            num3=temp%10
            candidate_digits=[num1,num2,num3]
            if all(digits.count(d) >= candidate_digits.count(d) for d in set(candidate_digits)):
                ans=num1*100+num2*10+num3
                result.append(ans)  
        return result 