class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        m, n = len(mana), len(skill)
        accumu = list(accumulate(skill, initial=0))
        tmp = 0
        for j in range(1, m):
            tmp += max(mana[j - 1] * accumu[i + 1] - mana[j] * accumu[i] for i in range(n))

        return tmp + accumu[-1] * mana[-1]
