def pascalTriangle(n):
    result=[[1]]
    for i in range(1, n):
        prev_row=result[-1]
        new_row=[1]
        for j in range(1, len(prev_row)):
            value=prev_row[j-1]+prev_row[j]
            new_row.append(value)
        new_row.append(1)
        result.append(new_row)

    return result


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return pascalTriangle(numRows)

        