public class Solution {
    public bool IsPalindrome(int x) {
        // Negative numbers and numbers ending with 0 (except 0 itself) cannot be palindromes
        if (x < 0 || (x != 0 && x % 10 == 0)) {
            return false;
        }

        int reversed = 0;
        int original = x;

        while (x > reversed) {
            reversed = reversed * 10 + x % 10;
            x /= 10;
        }
        return x == reversed || x == reversed / 10;
    }
}

