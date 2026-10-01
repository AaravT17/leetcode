class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        new_start, new_end = newInterval
        for i in range(len(intervals)):
            start, end = intervals[i]
            if new_end < start:
                res.append([new_start, new_end])
                return res + intervals[i:]
            elif new_start > end:
                res.append(intervals[i])
            else:
                new_start, new_end = min(new_start, start), max(new_end, end)

        res.append([new_start, new_end])
        return res
