# leetcode day 4 - August Challenge

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        import random
        
        if random.random() < 0.5:
            # Solution 1
            if num < 1:
                return False
            import math
            p = math.log(num, 4)
            if int(p) == p:
                return True
            else:
                return False
        else:
            # Solution 2
            if num == 1:
                return True
            elif num > 1:
                return self.isPowerOfFour(num/4)
            else:
                return False
