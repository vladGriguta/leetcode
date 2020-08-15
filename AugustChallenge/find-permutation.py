class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stack = []
        
        res = []
        
        for i in range(1,len(s)+1):
                stack.append(i)
                if s[i-1] == 'I':
                    while stack:
                        res.append(stack.pop())
        
        # tricky bit: if the last character is a 'D', then we would be left with a stack at the end of the
        # for loop above. one way around is to append the last digit in the stack separately and empty the
        # stack after
        stack.append(len(s)+1)
        while stack:
            res.append(stack.pop())
            
        return res
        