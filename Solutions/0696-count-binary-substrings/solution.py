class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # i, n = 0, len(s)
        # temp = []
        # result = 0

        # while n > i:
        #     count = 1
        #     while i + 1 < n and s[i] == s[i + 1]:
        #         count += 1
        #         i += 1
        #     temp.append(count)
        #     i += 1
        
        # for i in range(1, len(temp)):
        #     result += min(temp[i], temp[i - 1])

        # return result

        result, last, current = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
            else:
                result += min(last, current)
                last = current
                current = 1
        
        return result + min(last, current)
