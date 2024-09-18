class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(num) for num in nums]
    
        nums_str_len = len(nums_str)
        for i in range(nums_str_len):
            for j in range(0, nums_str_len - i - 1):
                if nums_str[j] + nums_str[j + 1] < nums_str[j + 1] + nums_str[j]:
                    # Swap if they are in the wrong order
                    nums_str[j], nums_str[j + 1] = nums_str[j + 1], nums_str[j]
        
        result = ''.join(nums_str)
        
        return '0' if result[0] == '0' else result

