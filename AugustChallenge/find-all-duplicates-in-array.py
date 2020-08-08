# Day 6 - August Challenge

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # the idea is to create a hashmap of the list. however, in constant space that is impossible
        # the catch is that we can leverage the fact that all values in the array are integers
        # in the range 1 -> size of array. Therefore, the list itself can become a hashmap, since each
        # position either correspond to a value in the array or is a duplicate of a value in the array
        
        # simplest way: for each position i, change the sign of the element on position nums[i]
        # if negative sign encountered, that element is a duplicate!
        
        res = []
        
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
            else:
                res.append(abs(nums[i]))
                
        return res
