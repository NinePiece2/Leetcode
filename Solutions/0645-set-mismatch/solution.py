class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        result = [0] * 2
        
        for i in range(1, n + 1):
            if count[i] == 2:
                result[0] = i
            if count[i] == 0:
                result[1] = i

        return result
