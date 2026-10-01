class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        removed = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prev_end:
                removed += 1
                prev_end = min(end, prev_end)
            else:
                prev_end = end
        return removed
