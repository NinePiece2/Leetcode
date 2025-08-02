from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        combined = count1 + count2

        for fruits, total in combined.items():
            if total % 2 != 0:
                return -1

        extra = []

        for fruits in combined:
            diff = count1[fruits] - count2[fruits]
            if diff > 0:
                extra.extend([fruits] * (diff // 2))
            elif diff < 0:
                extra.extend([fruits] * (-diff // 2))

        extra.sort()
        min_fruit = min(combined)

        total_swaps = len(extra) // 2

        cost = 0

        for i in range(total_swaps):
            cost += min(extra[i], min_fruit * 2)

        return cost
