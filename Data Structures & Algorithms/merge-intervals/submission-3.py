class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])

        h = []

        for i in intervals:
            if h and h[-1][1] >= i[0]:
                h[-1][1] = max(i[1], h[-1][1])
            else:
                h.append([i[0], i[1]])
        
        return h