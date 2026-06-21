class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = left = 0
        substr = {}

        for right, char in enumerate(s):
            if char in substr and substr[char] >= left:
                left = substr[char] + 1
            substr[char] = right
            counter = max(counter, right - left + 1)
        
        return counter
