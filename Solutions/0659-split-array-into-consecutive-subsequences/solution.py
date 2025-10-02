class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        dic = defaultdict(list)
        for num in nums:
            if cantidate := dic[num - 1]:
                heappush(dic[num], heappop(cantidate) + 1)
            else:
                heappush(dic[num], 1)
        return all(not val or val and val[0] > 2 for val in dic.values())
