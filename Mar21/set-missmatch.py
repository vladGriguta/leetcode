class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = 2*[0]
        d = collections.Counter(nums)
        for i in range(1,len(nums)+1):
            if d[i]>1:
                res[0] = i
            if i not in d.keys():
                res[1] = i
        return res
        