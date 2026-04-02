class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]
        

        for a, b in intervals[1:]:
            if a >= prevEnd:
                prevEnd = b
            else:
                res += 1
                prevEnd = min(b,prevEnd)
        return res