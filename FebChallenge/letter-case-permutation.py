class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        import itertools
        letter_idx = [i for i in range(len(S)) if S[i].isalpha()]
        res = []
        for permutation in itertools.product("01", repeat=len(letter_idx)):
            current_string = ''
            for i in range(len(S)):
                if i not in letter_idx:
                    current_string = current_string + S[i]
                else:
                    if permutation[letter_idx.index(i)] == '0':
                        current_string = current_string + S[i].lower()
                    elif permutation[letter_idx.index(i)] == '1':
                        current_string = current_string + S[i].upper()
                
            res.append(current_string)
        
        return res
