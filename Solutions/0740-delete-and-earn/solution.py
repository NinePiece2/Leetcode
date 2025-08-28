class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = 0

        for num in nums:
            max_num = max(max_num, num)
        
        total = [0] * (max_num + 1)
        for num in nums:
            total[num] += num
        
        first = total[0]
        second = max(total[0], total[1])

        for i in range(2, max_num + 1):
            current = max(first + total[i], second)
            first = second
            second = current
        
        return second
