class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        result = []

        for val in nums2:
            if count[val]:
                result.append(val)
                count[val] -= 1
        
        return result
