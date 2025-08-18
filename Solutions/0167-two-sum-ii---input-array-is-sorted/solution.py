class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        # for i in range(n - 1):
        #     search = target - numbers[i]
        #     found_index = bisect_left(numbers, search, lo=i+1) # i+1 for 1 indexing
        #     if found_index < n and numbers[found_index] == search:
        #         return [i + 1, found_index + 1] # +1 for 1 indexing
        left, right = 0, n - 1
        while right > left:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                break
            if curr_sum < target:
                left += 1
            else:
                right -= 1
            
        return [left + 1, right + 1]

