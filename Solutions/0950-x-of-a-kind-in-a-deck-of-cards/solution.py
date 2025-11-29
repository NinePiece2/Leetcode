class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # count = Counter(deck)
        # n = len(deck)
        # for i in range(2, n + 1):
        #     if n % i == 0:
        #         if all(val % i == 0 for val in count.values()):
        #             return True
        # return False
        count = Counter(deck)
        return reduce(gcd, count.values()) >= 2
