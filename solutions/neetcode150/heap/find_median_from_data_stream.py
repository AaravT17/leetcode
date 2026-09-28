import heapq


class MedianFinder:
    def __init__(self):
        self.smaller_half = []  # max heap that stores the smaller half of the elements in the data stream
        self.larger_half = []  # min heap that stores the larger half of the elements in the data stream

    def addNum(self, num: int) -> None:
        if self.larger_half and num >= self.larger_half[0]:
            heapq.heappush(self.larger_half, num)
        else:
            heapq.heappush(self.smaller_half, -num)

        if len(self.larger_half) - len(self.smaller_half) > 1:
            heapq.heappush(self.smaller_half, -heapq.heappop(self.larger_half))
        elif len(self.smaller_half) - len(self.larger_half) > 1:
            heapq.heappush(self.larger_half, -heapq.heappop(self.smaller_half))

    def findMedian(self) -> float:
        if len(self.smaller_half) == len(self.larger_half):
            return (-self.smaller_half[0] + self.larger_half[0]) / 2
        elif len(self.smaller_half) > len(self.larger_half):
            return float(-self.smaller_half[0])
        else:
            return float(self.larger_half[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
