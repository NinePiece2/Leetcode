class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        array = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            val1 = int(num1[i])
            for j in range(n - 1, -1, -1):
                val2 = int(num2[j])
                array[i + j + 1] += val1 * val2
        
        for i in range(m + n - 1, 0, -1):
            array[i - 1] += array[i] // 10
            array[i] %= 10

        i = 0 if array[0] else 1
        return "".join(str(val) for val in array[i:])
