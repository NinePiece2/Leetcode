class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        degree = count.most_common()[0][1]
        result = float('inf')
        print(degree)

        left, right = {}, {}
        for i, val in enumerate(nums):
            if val not in left:
                left[val] = i
            right[val] = i
        
        for val in nums:
            if count[val] == degree:
                tmp = right[val] - left[val] + 1
                if result > tmp:
                    result = tmp
            
        return result
