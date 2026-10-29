class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        result=[]
        for i in range(m):
            temp=''
            for j in range(n):
                if i==0:
                    temp+='.'
                elif j+1!=n and i!=0:
                    temp+='#'
                else:
                    temp+='.'
            temp=str(temp)
            result.append(temp)

        return result
            
                

        