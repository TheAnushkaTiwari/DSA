def check_if_ballons(text):
    letter={'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
    for char in text:
        if char in letter:
            letter[char]+=1
    return min(letter['b'], letter['a'], letter['l']//2, letter['o']//2, letter['n'])

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return check_if_ballons(text)
        