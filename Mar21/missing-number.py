class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(1) space complexity
        # O(n) runtime complexity
        # idea: the missing number should be identified as the difference between the sum of numbers 1 to n
        # and the sum of nums
        return int(0.5*len(nums)*(len(nums)+1))-sum(nums)