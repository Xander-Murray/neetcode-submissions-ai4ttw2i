class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, (start, end) in enumerate(intervals):
            # if current int we  are looking ats end is smaller than news start
            if end < newInterval[0]:
                res.append([start,end])
            # if currents start is greater than new end
            elif newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                # we need to merge
                newInterval = [
                    min(newInterval[0], start),
                    max(newInterval[1], end)
                ]
        # we only reach this if we have to merge or if we reach the end before adding the new interval
        res.append(newInterval)
        return res
            # 3 choices,
            # 1. newInterval will go inbetween this one and the next one
            # 2. newInterval needs to merge with the one we just added to res
            # 3.
        