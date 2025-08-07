class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str, num_open: int, num_closed: int):
            if len(current) == n * 2: # last bracket
                result.append(current)
                return
            if num_open < n:
                backtrack(current + '(', num_open + 1, num_closed)
            if num_open > num_closed:
                backtrack(current + ')', num_open, num_closed + 1)
        
        backtrack("", 0, 0)
        return result
