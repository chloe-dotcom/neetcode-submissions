class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
        
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)
        cooldown = deque()

        time = 0
        while cooldown or maxHeap:
            time += 1
            if cooldown and cooldown[0][1] <= time:
                cnt, _ = cooldown.popleft()
                heapq.heappush(maxHeap, cnt)

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt < 0:
                    cooldown.append((cnt, time + n+1))
            else:
                continue
        return time