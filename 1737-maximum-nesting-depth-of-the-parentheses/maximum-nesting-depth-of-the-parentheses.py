class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth=curr_depth=0
        opening_parantheses=0
        closing_parantheses=0
        for char in s:
            if char=='(':
                opening_parantheses+=1
            elif char==')':
                closing_parantheses+=1
            curr_depth=opening_parantheses-closing_parantheses
            if curr_depth>max_depth:
                max_depth=curr_depth
        return max_depth