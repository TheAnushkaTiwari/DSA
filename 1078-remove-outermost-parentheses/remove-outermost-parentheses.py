class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        level=0
        result=''
        for char in s:
            if char==')':
                level-=1
            if level>0:
                result+=char
            if char=='(':
                level+=1
        return result
        