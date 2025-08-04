from bisect import bisect_left, bisect_right

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        position = [p for p, _ in fruits]
        prefix = [0]

        for _, amount in fruits:
            prefix.append(prefix[-1] + amount)
        
        def get_sum(left:int, right:int):
            l = bisect_left(position, left)
            r = bisect_right(position, right)
            return prefix[r] - prefix[l]

        max_fruits = 0
        for i in range(0, k + 1):
            if k - 2 * i >= 0:
                max_fruits = max(max_fruits, get_sum(startPos - i, startPos + (k - 2 * i)))
                
            if k - 2 * i >= 0:
                max_fruits = max(max_fruits, get_sum(startPos - (k - 2 * i), startPos + i))

        return max_fruits
