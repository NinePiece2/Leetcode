class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_queue = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heappush(self.min_queue, val)
        if len(self.min_queue) > self.k:
            heappop(self.min_queue)
        return self.min_queue[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
