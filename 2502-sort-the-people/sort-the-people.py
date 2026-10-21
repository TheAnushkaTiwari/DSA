class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n=len(names)
        for i in range(n-1):
            for j in range(n-1):
                if heights[j]<heights[j+1]:
                    names[j], names[j+1]= names[j+1], names[j]
                    heights[j], heights[j+1]= heights[j+1], heights[j]
        return names

        