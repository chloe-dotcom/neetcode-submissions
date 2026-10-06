class TimeMap:

    def __init__(self):
        self.main = defaultdict(list) #[(time, value)]        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.main[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.main:
            return ""
        availableTimes = self.main[key]
        l = 0
        r = len(availableTimes)-1
        res = ""
        while l <= r:
            m = (l+r)//2
            current = availableTimes[m][0]
            if current == timestamp:
                return self.main[key][m][1]
            if current < timestamp:
                res = self.main[key][m][1]
                l = m + 1
            else:
                r = m - 1
        return res
