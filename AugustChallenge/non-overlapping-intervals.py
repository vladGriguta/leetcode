class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # example of greedy algorithm
        # it suffices to sort the intervals by the end time and iteratively delete those overlapping
        
        startTime = -sys.maxsize
        countIntervals = 0
        
        intervals = sorted(intervals, key = lambda interval: interval[1])
        
        for interval in intervals:
            if interval[0] >= startTime:
                countIntervals += 1
                startTime = interval[1]
        
        return len(intervals) - countIntervals
        