# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums FROM 
(SELECT num , LEAD(num) OVER (ORDER BY id) AS leads, LAG(num) OVER (ORDER BY ID) AS lags FROM Logs)t WHERE num=leads AND num=lags ;