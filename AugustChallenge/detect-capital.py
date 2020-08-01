class Solution:
    def detectCapitalUse(self, word: str) -> bool:
    	# 1st August 2020 Leetcode Challenge

        capitals = word[-1].isupper()
        
        if (word[0].islower() and capitals):
            return False
        
        for char in word[1:-1]:
            if char.isupper() != capitals:
                return False
        
        return True