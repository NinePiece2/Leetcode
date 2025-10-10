class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hash_table = {}

        for x in nums2[::-1]:
            while stack and stack[-1] < x:
                stack.pop()
            if stack:
                hash_table[x] = stack[-1]
            stack.append(x)
        
        return [hash_table.get(x, -1) for x in nums1]
