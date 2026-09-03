class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        have = set()
        for trip in triplets:
            if target[0] < trip[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            
            for i, v in enumerate(trip):
                if v == target[i]:
                    have.add(i)
            
            if len(have) == 3:
                return True
         
        return len(have) == 3
            