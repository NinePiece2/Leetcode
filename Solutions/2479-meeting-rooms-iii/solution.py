class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        idle = list(range(n))
        is_busy = []
        heapify(idle)
        count = [0] * n

        for start, end in meetings:
            while is_busy and is_busy[0][0] <= start:
                heappush(idle, heappop(is_busy)[1])
            i = 0
            if idle:
                i = heappop(idle)
                heappush(is_busy, (end, i))
            else:
                time_end, i = heappop(is_busy)
                heappush(is_busy, (time_end + end - start, i))
            count[i] += 1
        
        result = 0
        for i in range(n):
            if count[result] < count[i]:
                result = i
        
        return result
