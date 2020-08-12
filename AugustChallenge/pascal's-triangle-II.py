# Day 12 - August Challenge
# O(k) space solution

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # initialize result
        if rowIndex == 0: return [1]
        res = [1,1]
        for k in range(rowIndex-1):
            res.insert(-1,res[-2]+res[-1])
            for i in range(len(res)-3,0,-1):
                res[i] = res[i-1] + res[i]
        return res
