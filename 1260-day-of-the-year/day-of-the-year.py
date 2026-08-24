class Solution:
    def dayOfYear(self, date: str) -> int:
        year=int(date[:4])
        month=int(date[5:7])
        day=int(date[8:])
        result=0
        is_leap = (year%400==0) or (year%100!=0 and year%4==0)
        if is_leap:
            day_in_month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        result=day
        for i in range(1,month):
            result+=day_in_month[i]
        return result
        