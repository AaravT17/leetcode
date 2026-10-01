class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for start, end in intervals:
            if not res:
                res.append([start, end])
            else:
                prev_start, prev_end = res[-1]
                if start > prev_end:
                    res.append([start, end])
                else:
                    res[-1][1] = max(end, prev_end)
        return res
