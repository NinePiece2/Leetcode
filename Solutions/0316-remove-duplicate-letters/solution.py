class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_map = {val : i for i, val in enumerate(s)}
        stack = []
        vals = set()

        for i, ch in enumerate(s):
            if ch in vals:
                continue
            while stack and stack[-1] > ch and last_map[stack[-1]] > i:
                vals.remove(stack.pop())
            stack.append(ch)
            vals.add(ch)
        return "".join(stack)
