class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [(p / t - (p + 1) / (t + 1), p, t) for p, t in classes]
        heapify(heap)

        for _ in range(extraStudents):
            _, p, t = heappop(heap)
            p, t = p + 1, t + 1
            heappush(heap, (p / t - (p + 1) / (t + 1), p, t))

        return sum(vals[1] / vals[2] for vals in heap) / len(classes)
