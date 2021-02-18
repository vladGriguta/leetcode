class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        import math
        # split list in aritmetic sequences
        # an aritmetic sequence of size n can be split in (n-2)(n-1)/2 aritmetic sequences
        if len(A) < 3:
            return 0
        diff = A[1] - A[0]
        num_sequences = 0
        current_sequence_size = 2
        for i in range(2,len(A)):
            if A[i]-A[i-1] == diff:
                current_sequence_size += 1
            else:
                diff = A[i]-A[i-1]
                if current_sequence_size > 2:
                    num_sequences += (current_sequence_size-2)*(current_sequence_size-1)/2
                current_sequence_size = 2
        
        if current_sequence_size > 2:
            num_sequences += (current_sequence_size-2)*(current_sequence_size-1)/2
            
        return int(num_sequences)