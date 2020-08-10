class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        exp = 0
        for char in s[::-1]:
            res = res + (1 + ord(char)-ord('A')) * (26**exp)
            exp = exp + 1
        return res
