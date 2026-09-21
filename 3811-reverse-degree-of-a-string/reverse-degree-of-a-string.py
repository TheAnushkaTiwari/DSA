class Solution:
    def reverseDegree(self, s: str) -> int:
        result=0
        idx=1
        for char in s:
            value=26-(ord(char.lower())-97)
            result+=value*idx
            idx+=1
        return result