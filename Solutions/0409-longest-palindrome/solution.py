class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        odd_appearances = defaultdict(int)

        for char in s:
            odd_appearances[char] ^= 1
            count += 1 if odd_appearances[char] else -1
        
        return len(s) - count + 1 if count else len(s)

        # length = 0
        # letters = {}
        # max_odd_num = 0

        # for char in s:
        #     letters[char] = letters.get(char, 0) + 1

        # for val in letters.values():
        #     length += ((val // 2) * 2)
        #     if val % 2 == 1:
        #         max_odd_num = max(max_odd_num, val)

        # if max_odd_num != 0:
        #     length += 1
        # return length 
