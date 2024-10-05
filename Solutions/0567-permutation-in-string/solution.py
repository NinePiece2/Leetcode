from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)

        if (s1_len > s2_len):
            return False
        
        s1_count = Counter(s1)

        # sliding window
        window = Counter(s2[:s1_len])

        if (s1_count == window):
            return True

        for i in range (s1_len, s2_len):
            window[s2[i]] += 1

            window[s2[i - s1_len]] -= 1

            if (window[s2[i - s1_len]] == 0):
                del window[s2[i - s1_len]]
            
            if (s1_count == window):
                return True
        return False
