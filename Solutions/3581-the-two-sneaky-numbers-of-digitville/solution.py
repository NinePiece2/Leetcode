class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # count = Counter(nums)
        # most_common = count.most_common()
        # return [most_common[0][0], most_common[1][0]]
        visited = set()
        result = []
        for num in nums:
            if num in visited:
                result.append(num)
            visited.add(num)
        
        return result
