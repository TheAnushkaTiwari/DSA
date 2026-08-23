class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp=n
        sum_of_digits=0
        product=1
        while temp>0:
            digit=temp%10
            sum_of_digits+=digit
            product*=digit
            temp=temp//10
        check=sum_of_digits+product
        if check==0:
            return False
        return (n%check==0)
