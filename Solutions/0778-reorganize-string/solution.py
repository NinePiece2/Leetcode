class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        count = Counter(s)
        highest_num = max(count.values())

        if highest_num > (n + 1)//2:
            return ""

        i = 0
        result = [None]*n
        for val, occurances in count.most_common():
            while occurances:
                result[i] = val
                occurances -= 1
                i += 2
                if i >= n:
                    i = 1
        return ''.join(result)


