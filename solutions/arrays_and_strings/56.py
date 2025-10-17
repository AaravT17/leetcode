from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])

        result = []

        i = 0
        while i < len(intervals):
            start = i
            end_val = intervals[start][1]
            while i < len(intervals) - 1 and end_val >= intervals[i + 1][0]:
                i += 1
                end_val = max(intervals[i][1], end_val)
            result.append([intervals[start][0], end_val])
            i += 1

        return result
