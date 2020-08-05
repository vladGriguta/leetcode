# day 3 - leetcode August Challenge

class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^A-Za-z0-9]+', '', s).lower()
        
        if s[::-1]==s:
            return True
        else:
            return False
