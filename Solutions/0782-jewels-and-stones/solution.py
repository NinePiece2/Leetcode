class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # count = 0
        # set_stones = Counter(stones)
        # for i, num in set_stones.items():
        #     if i in jewels:
        #         count += num
        # return count
        set_jewels = set(jewels)
        return sum(char in set_jewels for char in stones)
