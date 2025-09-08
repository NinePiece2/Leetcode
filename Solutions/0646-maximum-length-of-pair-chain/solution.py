class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=(lambda x : x[1]))
        result, last = 0, -inf

        for val1, val2 in pairs:
            if last < val1:
                result += 1
                last = val2

        return result
