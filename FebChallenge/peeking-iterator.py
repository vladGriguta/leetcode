# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.base_iterator = iterator
        self.peeked_elem = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peeked_elem:
            self.peeked_elem = self.base_iterator.next()
        return self.peeked_elem
        

    def next(self):
        """
        :rtype: int
        """
        if not self.peeked_elem:
            return self.base_iterator.next()
        else:
            res = self.peeked_elem
            self.peeked_elem = None
            return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.base_iterator.hasNext() or bool(self.peeked_elem)
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
