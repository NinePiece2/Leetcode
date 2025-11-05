class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        dic = defaultdict(int)
        for start, end in flowers:
            dic[start] += 1
            dic[end + 1] -= 1
        
        m = len(people)
        set_nums = sorted(dic)
        result = [0] * m
        sum_val = 0
        i = 0
        
        for t, j in sorted(zip(people, range(m))):
            while i < len(set_nums) and set_nums[i] <= t:
                sum_val += dic[set_nums[i]]
                i += 1
            result[j] = sum_val

        return result
