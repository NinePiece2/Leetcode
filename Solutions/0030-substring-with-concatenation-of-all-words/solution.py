class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        count = Counter(words)
        m, n = len(s), len(words)
        k = len(words[0])
        result = []

        for i in range(k):
            left = right = i
            new_counter = Counter()
            while right + k <= m:
                text = s[right:right + k]
                right += k
                if count[text] == 0:
                    left = right
                    new_counter.clear()
                    continue
                
                new_counter[text] += 1
                while new_counter[text] > count[text]:
                    remember = s[left:left + k]
                    left += k
                    new_counter[remember] -= 1
                if right - left == k * n:
                    result.append(left)

        return result
