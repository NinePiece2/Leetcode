class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # arr.sort(key=lambda val: abs(val - x))
        # return sorted(arr[:k])

        left, right = 0, len(arr) - k

        while right > left:
            mid = (left + right) // 2
            if x - arr[mid] <= arr[mid + k] -x:
                right = mid
            else:
                left = mid +1

        return arr[left: left + k] 
