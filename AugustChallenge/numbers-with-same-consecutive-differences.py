class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        res = []
        
        def helperOpenBranch(prior,n,K):
            if n == 0:
                res.append(int(''.join(map(str,prior))))
            elif n > 0:
                if prior[-1] - K >= 0:
                    helperOpenBranch(prior+[prior[-1] - K],n-1,K)
                if prior[-1] + K < 10 and K!=0:
                    helperOpenBranch(prior+[prior[-1] + K],n-1,K)
                else:
                    pass
            else:
                # something should have gone wrong
                raise ValueError('unexpected error')
                    
        
        
        for i in range(1,10):
            helperOpenBranch([i],N-1,K)
        
        if N==1:
            res.append(0)
        
        return res

                
            