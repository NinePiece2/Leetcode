class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left, right = 0, n - 1

        while right >= left:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return letters[left % n]
