class Solution:
    def bestClosingTime(self, customers: str) -> int:
        result = 0
        min_pen = cost = customers.count("Y")
        for j, char in enumerate(customers, 1):
            cost += 1 if char == "N" else -1
            if cost < min_pen:
                result = j
                min_pen = cost

        return result                
            
