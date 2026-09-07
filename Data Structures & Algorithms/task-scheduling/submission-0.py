class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for i in tasks:
            freq[i] = freq.get(i, 0) + 1
        
        maxheap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxheap)
        print(f"{maxheap=}")
        
        cooldown = deque()
        time = 0
        while maxheap or cooldown:
            time += 1
            if not maxheap: 
                time = cooldown[0][1]
            else:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt:
                    cooldown.append([cnt, time + n])
            
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(maxheap, cooldown.popleft()[0])
        
        return time