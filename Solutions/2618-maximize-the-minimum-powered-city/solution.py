class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        f = [0] * (n + 1)
        for i, val in enumerate(stations):
            left, right = max(0, i - r), min(i + r, n - 1)
            f[left] += val
            f[right + 1] -= val
        
        s = list(accumulate(f))

        def checker(x, k):
            f = [0] * (n + 1)
            t = 0
            for i in range(n):
                t += f[i]
                dist = x - (s[i] + t)
                if dist > 0:
                    if k < dist:
                        return False
                    k -= dist
                    j = min(i + r, n - 1)
                    left, right = max(0, j - r), min(j + r, n - 1)
                    f[left] += dist
                    f[right + 1] -= dist
                    t += dist
            return True
        
        left, right = 0, 1 << 40
        while right > left:
            mid = (left + right + 1) // 2
            if checker(mid, k):
                left = mid
            else:
                right = mid - 1
        return left
