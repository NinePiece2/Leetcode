class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        vals = sorted(count.items(), key=lambda x: -x[1])
        return "".join(char * num for char, num in vals)
