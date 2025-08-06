class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        self.segment = [0] * (4 * n)
        self.n = n
        self.build(baskets, 0, n -1, 1)
        num_unplaced = 0
        for fruit in fruits:
            if self.find_and_use(fruit, 0, n - 1, 1) == -1:
                num_unplaced += 1
        return num_unplaced


    def build(self, baskets: List[int], low: int, high: int, index: int):
        if low == high:
            self.segment[index] = baskets[high]
        else:
            mid = (high + low)//2
            self.build(baskets, low, mid, index * 2)
            self.build(baskets, mid + 1, high, index * 2 + 1)
            self.segment[index] = max(self.segment[index * 2], self.segment[index * 2 + 1])
    
    def find_and_use(self, fruit: int, low: int, high: int, index: int) -> int:
        # seg can't fir the fruit
        if self.segment[index] < fruit:
            return -1
        # at the leaf use this basket
        if low == high:
            self.segment[index] = -1
            return 1
        
        mid = (high + low)//2
        if self.segment[index * 2] >= fruit:
            result = self.find_and_use(fruit, low, mid, index * 2)
        else:
            result = self.find_and_use(fruit, mid + 1, high, index * 2 + 1)
        self.segment[index] = max(self.segment[index * 2], self.segment[index * 2 + 1])
        return result
