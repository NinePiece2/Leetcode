class Solution:
    def minWindow(self, s: str, t: str) -> str:
        find = Counter(t)
        window = Counter()
        left = count = 0
        start, min_num = -1, inf

        for right, char in enumerate(s):
            window[char] += 1
            if find[char] >= window[char]:
                count += 1
            while count == len(t):
                if right - left + 1 < min_num:
                    min_num = right - left + 1
                    start = left
                if find[s[left]] >= window[s[left]]:
                    count -= 1
                window[s[left]] -= 1
                left += 1
        
        return "" if start < 0 else s[start:start + min_num]
