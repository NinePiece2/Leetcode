class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        n = len(power)
        count = Counter(power)
        power.sort()

        next_spell_index = [bisect_right(power, val + 2, lo=i + 1) for i, val in enumerate(power)]

        @cache
        def dfs(i):
            if i >= n:
                return 0
            val1 = dfs(i + count[power[i]])
            val2 = power[i] * count[power[i]] + dfs(next_spell_index[i])
            return max(val1, val2)

        return dfs(0)
