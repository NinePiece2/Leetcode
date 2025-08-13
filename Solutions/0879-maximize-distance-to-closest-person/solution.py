class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last = first = None
        max_dist = 0
        for i, someone in enumerate(seats):
            if someone:
                if last is not None:
                    max_dist = max(max_dist, i - last)
                if first is None:
                    first = i
                last = i
        return max(first, len(seats) - last - 1, max_dist // 2)
