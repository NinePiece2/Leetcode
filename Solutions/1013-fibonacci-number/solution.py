class Solution:
    def fib(self, n: int) -> int:
        def matrix_mul(a, b):
            return [
                [a[0][0] * b[0][0] + a[0][1] * b[1][0],
                a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                [a[1][0] * b[0][0] + a[1][1] * b[1][0],
                 a[1][0] * b[0][1] + a[1][1] * b[1][1]]
            ]
        
        def matrix_power(m, power):
            result = [[1, 0], [0, 1]]
            while power:
                if power & 1:
                    result = matrix_mul(result, m)
                m = matrix_mul(m, m)
                power >>= 1
            return result

        if n == 0:
            return 0
        
        base = [[1, 1], [1, 0]]
        result = matrix_power(base, n - 1)
        return result[0][0]
