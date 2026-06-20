class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        if not coins or k <= 0:
            return 0

        n = len(coins)
        segs = sorted(coins, key=lambda x: x[0])
        starts = [s[0] for s in segs]
        ends   = [s[1] for s in segs]
        amts   = [s[2] for s in segs]

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (ends[i] - starts[i] + 1) * amts[i]

        def money_up_to(x):
            if x < starts[0]:
                return 0
            idx = bisect.bisect_right(starts, x) - 1
            right = min(ends[idx], x)
            return prefix[idx] + (right - starts[idx] + 1) * amts[idx]

        cands = set()
        for i in range(n):
            cands.add(starts[i])
            cands.add(ends[i] - k + 1)

        best = 0
        for i in cands:
            i = max(1, i)
            best = max(best, money_up_to(i + k - 1) - money_up_to(i - 1))
        return best
