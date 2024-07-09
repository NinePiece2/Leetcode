class Solution:
    def mergesort(self, arr: List[int]):
        if len(arr) > 1:
            r = len(arr)//2
            leftArr = arr[:r]
            rightArr = arr[r:]

            self.mergesort(leftArr)
            self.mergesort(rightArr)

            i = j = k = 0

        
            while i < len(leftArr) and j < len(rightArr):
                if leftArr[i] < rightArr[j]:
                    arr[k] = leftArr[i]
                    i += 1
                else:
                    arr[k] = rightArr[j]
                    j += 1
                k += 1

        
            while i < len(leftArr):
                arr[k] = leftArr[i]
                i += 1
                k += 1

            while j < len(rightArr):
                arr[k] = rightArr[j]
                j += 1
                k += 1
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m]
        nums1.extend(nums2[:n])
        nums1.sort()
        #self.mergesort(nums1)
        #print(nums1)
        
    
        

