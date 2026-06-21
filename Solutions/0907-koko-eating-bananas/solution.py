class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # def checker(k: int) -> bool:
        #     return sum((val + k - 1) // k for val in piles) <= h
        
        # return bisect_left(range(1, max(piles) + 1), True, key=checker) + 1

        left, right = 1, max(piles)
        while left < right:
            k = (left + right) // 2

            hours_spent = 0
            for pile in piles:
                hours_spent += ceil(pile/k)
            
            if hours_spent <= h:
                right = k
            else:
                left = k + 1
        
        return left
