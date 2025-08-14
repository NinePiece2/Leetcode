class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        result = 0
        count = Counter()

        for i in range(len(s) - minSize + 1):
            temp = s[i : i + minSize]
            string_set = set(temp)
            if len(string_set) <= maxLetters:
                count[temp] += 1
                result = max(result, count[temp])
        
        return result
