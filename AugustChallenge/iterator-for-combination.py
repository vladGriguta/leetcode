# Day 13 - August Challenge

# cheated by using pre-defined function from itertoos
# also, storing all possible combinations so not memory efficient

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = [ch for ch in characters]
        self.combinationLength = combinationLength
        self.possiblePositions = []
        self.currentPos = -1

    def next(self) -> str:
        # initialize iterator
        if self.currentPos == -1:
            if self.combinationLength > len(self.characters):
                return ''
            elif self.combinationLength <= 0:
                return ''
            else:
                # initialize vector of possible positions
                self.currentPos += 1
                from itertools import combinations
                self.possiblePositions = sorted(combinations([i for i in range(len(self.characters))],self.combinationLength))
                return ''.join([self.characters[i] for i in list(self.possiblePositions[self.currentPos])])
        else:
            if self.hasNext():
                self.currentPos += 1
                return ''.join([self.characters[i] for i in list(self.possiblePositions[self.currentPos])])
            else:
                return ''
        
        

    def hasNext(self) -> bool:
        if self.currentPos == -1:
            if 0 < self.combinationLength < len(self.characters):
                return True
            else:
                return False
        elif self.currentPos < len(self.possiblePositions)-1:
            return True
        else:
            return False
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()