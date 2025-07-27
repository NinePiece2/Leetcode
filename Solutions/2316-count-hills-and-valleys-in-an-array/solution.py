class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        total = 0
        filteredNums = [nums[0]]
        for i in nums[1:]:
            if i != filteredNums[-1]:
                filteredNums.append(i)

        for i in range(1, len(filteredNums) - 1):
            if filteredNums[i] > filteredNums[i - 1] and  filteredNums[i] > filteredNums[i + 1]:
                total += 1
            elif filteredNums[i] < filteredNums[i - 1] and  filteredNums[i] < filteredNums[i + 1]:        
                total += 1

        return total
        
