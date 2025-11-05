class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        left = SortedList()
        right = SortedList()
        count = Counter()
        sum_val = 0
        n = len(nums)
        result = [0] * (n - k + 1)

        def add(val: int):
            if count[val] == 0:
                return
            temp = (count[val], val)
            if left and temp > left[0]:
                nonlocal sum_val
                sum_val += temp[0] * temp[1]
                left.add(temp)
            else:
                right.add(temp)

        def remove(val: int):
            if count[val] == 0:
                return
            temp = (count[val], val)
            if temp in left:
                nonlocal sum_val
                sum_val -= temp[0] * temp[1]
                left.remove(temp)
            else:
                right.remove(temp)

        for i, val in enumerate(nums):
            remove(val)
            count[val] += 1
            add(val)
            j = i - k + 1
            if j < 0:
                continue
            while right and len(left) < x:
                temp = right.pop()
                left.add(temp)
                sum_val += temp[0] * temp[1]

            while len(left) > x:
                temp = left.pop(0)
                sum_val -= temp[0] * temp[1]
                right.add(temp)
            result[j] = sum_val

            remove(nums[j])
            count[nums[j]] -= 1
            add(nums[j])

        return result
