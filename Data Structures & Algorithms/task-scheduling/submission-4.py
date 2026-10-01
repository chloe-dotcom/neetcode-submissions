class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1

        taskToCount = []
        heapq.heapify(taskToCount)
        for t, count in freq.items():
            heapq.heappush(taskToCount, -count)
        
        count = 0
        q = deque() # countdown: (-rem, when it is ready)
        while taskToCount or q:
            count += 1
            
            # countdown ready to be popped
            if q and q[0][1] == count:
                rem, _ = q.popleft()
                heapq.heappush(taskToCount, rem)

            if taskToCount:
                amountLeft = heapq.heappop(taskToCount) + 1
                if amountLeft < 0:
                    q.append((amountLeft, count + n + 1))
            else:
                continue
            
        return count