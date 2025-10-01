class MedianFinder:

    def __init__(self):
        self.min_queue = []
        self.max_queue = []

    def addNum(self, num: int) -> None:
        heappush(self.min_queue, -heappushpop(self.max_queue, -num))
        if len(self.min_queue) - len(self.max_queue) > 1:
            heappush(self.max_queue, -heappop(self.min_queue))

    def findMedian(self) -> float:
        if len(self.min_queue) == len(self.max_queue):
            return (self.min_queue[0] - self.max_queue[0]) / 2
        return self.min_queue[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
