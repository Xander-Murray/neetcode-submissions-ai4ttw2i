class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []

        for a, b in intervals:
            # add first interval or if the last one we added has a 
            # end number that is less 
            # than the one we arelooking at we can jsut add the whle interfval
            if not res or a >= res[-1][1] + 1:
                res.append([a, b])
            else:
                # if the end value of current is larger than the last end value 
                # we can just change it to the max of the last one
                if b > res[-1][1]:
                    res[-1][1] = b
        return res
        