class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # def pick_largest(nums: List[int], k: int) -> List[int]:
        #     n = len(nums)
        #     stack = [0] * k
        #     top = -1
        #     remain = n - k
        #     for num in nums:
        #         while top >= 0 and stack[top] < num and remain > 0:
        #             top -= 1
        #             remain -= 1
        #         if top + 1 < k:
        #             top += 1
        #             stack[top] = num
        #         else:
        #             remain -= 1
        #     return stack
        
        # def compare(nums1: List[int], nums2: List[int], i: int, j: int) -> bool:
        #     if i >= len(nums1):
        #         return False
        #     elif j >= len(nums2):
        #         return True
        #     elif nums1[i] > nums2[j]:
        #         return True
        #     elif nums1[i] < nums2[j]:
        #         return False
        #     else:
        #         return compare(nums1, nums2, i + 1, j + 1)
        
        # def merge(nums1: List[int], nums2: List[int]) -> List[int]:
        #     m, n = len(nums1), len(nums2)
        #     i = j = 0
        #     result = [0] * (m + n)
        #     for k in range(m + n):
        #         if compare(nums1, nums2, i, j):
        #             result[k] = nums1[i]
        #             i += 1
        #         else:
        #             result[k] = nums2[j]
        #             j += 1
        #     return result

        # m, n = len(nums1), len(nums2)
        # left, right = max(0, k - n), min(k, m)
        # result = [0] * k
        # for val in range(left, right + 1):
        #     temp = pick_largest(nums1, val)
        #     temp2 = pick_largest(nums2, k - val)
        #     temp3 = merge(temp, temp2)
        #     if result < temp3:
        #         result = temp3

        # return result

        def pick_largest(nums: List[int], val: int) -> List[int]:
            stack = []
            drop = len(nums) - val
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:val]
        
        def merge(nums1: List[int], nums2: List[int]) -> List[int]:
            result = []
            while nums1 or nums2:
                if nums1 > nums2:
                    result.append(nums1.pop(0))
                else:
                    result.append(nums2.pop(0))
            return result
        
        m, n = len(nums1), len(nums2)
        result = []
        for val in range(max(0, k - n), min(k, m) + 1):
            part1 = pick_largest(nums1, val)
            part2 = pick_largest(nums2, k - val)
            check = merge(part1, part2)
            result = max(result, check)
        return result
