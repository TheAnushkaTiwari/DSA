def roman_to_integer(s):
    roman_symbol_values={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    value=0
    for i in range(len(s)):
        if i+1<len(s) and roman_symbol_values[s[i]]<roman_symbol_values[s[i+1]]:
            value-=roman_symbol_values[s[i]]
        else:
            value+=roman_symbol_values[s[i]]
    return value


class Solution:
    def romanToInt(self, s: str) -> int:
        return roman_to_integer(s)
        