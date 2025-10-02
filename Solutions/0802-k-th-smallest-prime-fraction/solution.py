class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = [(1 / num, 0, i + 1) for i, num in enumerate(arr[1:])] # the first num is always 1
        heapify(heap)

        for _ in range(k - 1):
            _, i, j = heappop(heap)
            if i + 1 < j:
                heappush(heap, (arr[i + 1] / arr[j], i + 1, j))

        return [arr[heap[0][1]], arr[heap[0][2]]]
