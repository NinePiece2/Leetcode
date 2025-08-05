from collections import defaultdict

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        num_unplaced = 0
        used = [False]*n

        for fruit in fruits:
            placed = False
            for i in range(n):
                if not used[i] and fruit <= baskets[i]:
                    used[i] = True
                    placed = True
                    break
            if not placed:
                num_unplaced += 1
        return num_unplaced

