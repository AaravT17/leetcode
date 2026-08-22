class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Brute force
        # n = len(heights)
        # largest = 0
        # for i in range(n):
        #     min_height = heights[i]
        #     j = i
        #     while j < n:
        #         min_height = min(heights[j], min_height)
        #         largest = max(largest, (j - i + 1) * min_height)
        #         j += 1

        # return largest
        # Time: O(n^2), Space: O(1)

        n = len(heights)
        largest = 0
        stack = []  # monotonic increasing stack, stores (start index, height)
        for i, h in enumerate(heights):
            start = i  # the earliest index at which we can start a rectangle of height h
            while stack and stack[-1][1] > h:
                prev_i, prev_h = stack.pop()
                # calculate area
                area = prev_h * (i - prev_i)  # width does not include i since heights[i] is shorter
                largest = max(largest, area)
                start = prev_i  # prev_h > h, so it can be included in a rectangle of height h
            if not stack or stack[-1][1] < h:
                stack.append((start, h))

        # each unpopped element forms a rectangle of height h and width (n - i) (no shorter wall encountered after)
        for i, h in stack:
            largest = max(largest, (n - i) * h)

        return largest
        # Time: O(n), Space: O(n)
