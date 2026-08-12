class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount+1) for _ in range(len(coins))]

        def dfs(i, curr):
            if curr == amount:
                return 1

            if i >= len(coins) or curr > amount:
                return 0
            
            if dp[i][curr] != -1:
                return dp[i][curr]
            
            dp[i][curr] = dfs(i, curr + coins[i]) + dfs(i+1, curr)
            return dp[i][curr]
        
        return dfs(0, 0)