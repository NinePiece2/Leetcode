class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        delta = (sum(aliceSizes) - sum(bobSizes)) // 2
        bob_set = set(bobSizes)
        for alice_candy in aliceSizes:
            if (bob_candy := alice_candy - delta) in bob_set:
                return [alice_candy, bob_candy]
