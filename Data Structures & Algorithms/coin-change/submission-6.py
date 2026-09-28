class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        q = deque()
        q.append(0)
        res = 0
        seen = [False for _ in range(amount+1)]
        seen[0] = True

        while q:
            res += 1
            for i in range(len(q)):
                currAmount = q.popleft()
                for c in coins:
                    nxt = currAmount + c
                    if nxt == amount:
                        return res
                    if nxt > amount or seen[nxt]:
                        continue
                    seen[nxt] = True
                    q.append(nxt)

        return -1