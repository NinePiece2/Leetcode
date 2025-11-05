class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # sorted_list = SortedList()
        # result = j = 0
        # for i, val in enumerate(nums):
        #     sorted_list.add(val)
        #     while sorted_list[-1] - sorted_list[0] > limit:
        #         sorted_list.remove(nums[j])
        #         j += 1
        #     result = max(result, i - j + 1)
        # return result

        min_queue = Deque()
        max_queue = Deque()
        left = 0
        n = len(nums)
        for right, val in enumerate(nums):
            while max_queue and nums[max_queue[-1]] < val:
                max_queue.pop()
            while min_queue and nums[min_queue[-1]] > val:
                min_queue.pop()

            min_queue.append(right)
            max_queue.append(right)

            if nums[max_queue[0]] - nums[min_queue[0]] > limit:
                left += 1
                if max_queue[0] < left:
                    max_queue.popleft()
                if min_queue[0] < left:
                    min_queue.popleft()

        return n - left
