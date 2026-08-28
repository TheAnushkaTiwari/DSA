class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acronym=''
        for i in range(len(words)):
            word=words[i]
            acronym+=word[0]
        return acronym==s
        