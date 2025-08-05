import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half_x = 0
        while x > reversed_half_x:
            reversed_half_x = reversed_half_x * 10 + x%10
            x //= 10

        return reversed_half_x == x or reversed_half_x//10 == x 
