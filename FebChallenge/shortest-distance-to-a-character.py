from typing import List
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        max_size = 1e4
        # plan: iterate the string twice, compute the distance and assign the minimum distance of the 2 iterations
        leftwise, rightwise = [], []
        last_index_found_left = max_size
        last_index_found_right = max_size
        for i in range(len(s)):
            if s[i] == c:
                last_index_found_left = i
            leftwise.append(i-last_index_found_left if last_index_found_left!=max_size else last_index_found_left)
            
            bakward_i = len(s)-i-1
            if s[bakward_i] == c:
                last_index_found_right = bakward_i
            rightwise.insert(0,last_index_found_right-bakward_i if last_index_found_right!=max_size else last_index_found_right)
        
        return [min(lel, rel) for lel, rel in zip(leftwise, rightwise)]

assert Solution().shortestToChar("loveleetcode","e") == [3,2,1,0,1,0,0,1,2,2,1,0]