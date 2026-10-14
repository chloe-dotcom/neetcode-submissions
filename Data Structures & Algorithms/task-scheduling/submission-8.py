class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
        
        available = [(-1 * cnt) for _, cnt in freq.items()]
        heapq.heapify(available)

        waiting = deque()
        time = 0
        while available or waiting:
            time += 1
            if waiting and waiting[0][1] <= time:
                task, time_now = waiting.popleft()
                heapq.heappush(available, task)
            
            if not available:
                continue
            
            remaining = heapq.heappop(available) + 1
            if remaining < 0:
                waiting.append((remaining, n + time + 1))
        
        return time