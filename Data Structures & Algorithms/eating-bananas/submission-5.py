class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return 0

        maxK = max(piles)
        minK = 1
        best = maxK

        while minK <= maxK:
            current_k = int((minK + maxK)//2)
            current_time = 0
            for group in piles:
                current_time += math.ceil(group / current_k)

            # print(current_k, current_time)
            if current_time > h:
                minK = current_k + 1
            
            # if current_time < h:
            else:
                best = current_k
                maxK = current_k - 1
        
        return best