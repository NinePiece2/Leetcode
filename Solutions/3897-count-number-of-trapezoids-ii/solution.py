class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        slope_to_intercept = defaultdict(list)
        mid_to_slope = defaultdict(list)
        result = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                if x2 == x1:
                    m = float('inf')
                    b = x1
                else:
                    m = (y2 - y1) / (x2 - x1)
                    b = (y1 * dx -x1 * dy) / dx

                mid = (x1 + x2) * 10000 + y2 + y1
                slope_to_intercept[m].append(b)
                mid_to_slope[mid].append(m)
        
        for sti in slope_to_intercept.values():
            if len(sti) == 1:
                continue
            
            count = defaultdict(int)
            for b_val in sti:
                count[b_val] += 1
            
            total_sum = 0
            for count in count.values():
                result += total_sum * count
                total_sum += count
            
        for mts in mid_to_slope.values():
            if len(mts) == 1:
                continue

            count = defaultdict(int)
            for m_val in mts:
                count[m_val] += 1

            total_sum = 0
            for count in count.values():
                result -= total_sum * count
                total_sum += count
        
        return result
