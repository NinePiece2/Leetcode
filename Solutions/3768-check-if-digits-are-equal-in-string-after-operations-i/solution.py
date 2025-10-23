class Solution:
    def hasSameDigits(self, s: str) -> bool:
        temp_list = list(map(int, s))
        n = len(s)
        for i in range(n - 1, 1, -1):
            for j in range(i):
                temp_list[j] = (temp_list[j] + temp_list[j + 1]) % 10
        return temp_list[0] == temp_list[1]
