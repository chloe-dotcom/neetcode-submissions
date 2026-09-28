class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        q = deque([amount])
        visited = [False for _ in range(amount + 1)]
        visited[amount] = True
        res = 0

        while q:
            for _ in range(len(q)):
                rem = q.popleft()
                if rem == 0:
                    return res
                for c in coins:
                    nxt = rem - c
                    if nxt < 0 or visited[nxt]:
                        continue
                    q.append(nxt)
                    visited[nxt] = True
            res += 1
        return -1