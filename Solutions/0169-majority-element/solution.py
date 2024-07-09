class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # temp: Dict[int, int] = {}

        # for i in range(0, len(nums)):
        #     if (nums[i] in temp):
        #         a = temp[nums[i]] + 1
        #         temp[nums[i]] = a
        #     else:
        #         temp[nums[i]] = 1

        # sorted_values =  dict(sorted(temp.items(), key=lambda item: item[1], reverse=True))
        # first_key = next(iter(sorted_values.keys()))

        # return first_key

        nums.sort()
        return nums[len(nums)//2]
    
    def quicksort(self, arr: List[int]):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            left = [x for x in arr[1:] if x < pivot]
            right = [x for x in arr[1:] if x >= pivot]
            return self.quicksort(left) + [pivot] + self.quicksort(right)
        
