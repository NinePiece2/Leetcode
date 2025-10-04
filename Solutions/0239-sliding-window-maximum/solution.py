class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # queue = [(-val, i) for i, val in enumerate(nums[: k - 1])]
        # heapify(queue)
        # result = []

        # for i in range(k - 1, len(nums)):
        #     heappush(queue, (-nums[i], i))
        #     while queue[0][1] <= i - k:
        #         heappop(queue)
        #     result.append(-queue[0][0])

        # return result

        queue = deque()
        result = []
        for i, val in enumerate(nums):
            if queue and i - queue[0] >= k:
                queue.popleft()

            while queue and nums[queue[-1]] <= val:
                queue.pop()
            queue.append(i)
            
            if i >= k - 1:
                result.append(nums[queue[0]])
        
        return result
