from typing import List
import numpy as np
import pandas as pd
import time

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # plan: sort array and return the length of the longest two successive values
        res = 0
        # construct a dictionary of the appearances
        import pandas as pd
        vals_dict = pd.value_counts(nums)

        for key in vals_dict:
        	if key+1 in vals_dict:
        		res = max(res, vals_dict[key]+vals_dict[key+1])
        return res


assert Solution().findLHS([1,3,2,2,5,2,3,7]) == 5
assert Solution().findLHS([1,2,3,4]) == 2
assert Solution().findLHS([1,1,1,1]) == 0

long_arr = np.random.randint(0,1e9,2*10000).tolist()
t = time.time()
Solution().findLHS(long_arr)
print('Operation took {:.2f} seconds'.format(time.time()-t))