class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        m, n = len(s), len(goal)
        if m != n:
            return False

        count_s, count_goal = Counter(s), Counter(goal)
        if count_s != count_goal:
            return False
        
        diff = sum(s[i] != goal[i] for i in range(n))
        return diff == 2 or (diff == 0 and any(val > 1 for val in count_s.values()))
