# Day 14 - August Challenge

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # idea: maximum palindrome is the size of the string minus the number of characters
        # that appear an odd number of times plus 1
        
        # if all characters with an even number of appearances, max palindrome is the length of the string
        
        # convention: odd -> -1, even -> 1
        mapEven = {}
        for ch in s:
            if ch not in mapEven:
                mapEven[ch] = -1
            else: 
                mapEven[ch] *= -1
        
        if -1 in mapEven.values():
            return len(s) - (sum(value == -1 for value in mapEven.values()) - 1)
        else:
            return len(s)
