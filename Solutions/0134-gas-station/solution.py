class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = j = n - 1
        count = sum_val = 0
        while count < n:
            sum_val += gas[j] - cost[j]
            count += 1
            j = (j + 1) % n
            while sum_val < 0 and count < n:
                i -= 1
                sum_val += gas[i] - cost[i]
                count += 1
        return -1 if sum_val < 0 else i 
