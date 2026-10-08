class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # how many coins it takes to make ith amount
        dp = [(amount + 1) for _ in range(amount + 1)]
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(1 + dp[a-c], dp[a])

        return -1 if dp[amount] == (amount+1) else dp[amount]