class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        queue = [[val + nums2[0], i, 0] for i, val in enumerate(nums1[:k])]
        result = []
        heapify(queue)

        while queue and k > 0:
            _, i, j = heappop(queue)
            result.append([nums1[i], nums2[j]])
            k -= 1

            if j + 1 < len(nums2):
                heappush(queue, [nums1[i] + nums2[j + 1], i, j + 1])

        return result
