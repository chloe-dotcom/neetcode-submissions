class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)
        
        cooldown = deque() # (-cnt, time when ready)
        time = 0
        while maxHeap or cooldown:
            time += 1
            if cooldown and cooldown[0][1] == time:
                rem, _ = cooldown.popleft()
                heapq.heappush(maxHeap, rem)
            
            if maxHeap:
                count = heapq.heappop(maxHeap)+1
                # we have more of this task
                if count < 0:
                    cooldown.append((count, time + n + 1))
            else:
                continue
        
        return time