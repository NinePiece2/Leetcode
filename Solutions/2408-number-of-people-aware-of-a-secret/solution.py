class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * n
        dp[0] = 1
        count = 0

        for i in range(delay, n):
            count += dp[i - delay]
            dp[i] = count

            if i - forget + 1 >= 0:
                count -= dp[i - forget + 1]
                
        return sum(dp[-forget:]) % (10 ** 9 + 7)
