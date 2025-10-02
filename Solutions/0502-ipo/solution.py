class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap1 = [(cap, prof) for cap, prof in zip(capital, profits)]
        heapify(heap1)

        heap2 = []

        while k:
            while heap1 and heap1[0][0] <= w:
                heappush(heap2, -heappop(heap1)[1])
            
            if not heap2:
                break

            w -= heappop(heap2)
            k -= 1
        
        return w
