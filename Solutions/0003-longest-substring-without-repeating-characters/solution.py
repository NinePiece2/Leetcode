class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        top = {}
        counter = left = 0

        for right, char in enumerate(s):
            if char in top and top[char] >= left:
                left = top[char] + 1
            top[char] = right
            counter = max(counter, right - left + 1)
        
        return counter
