class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'

        for _ in range(n - 1):
            i = 0
            tmp = []
            while i < len(result):
                j = i
                while j < len(result) and result[j] == result[i]:
                    j += 1
                tmp.append(str(j - i))
                tmp.append(str(result[i]))
                i = j
            result = ''.join(tmp)

        return result
