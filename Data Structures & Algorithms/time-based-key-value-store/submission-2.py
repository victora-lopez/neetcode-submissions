from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, timestamps = "", self.time_map.get(key, [])
        l, r = 0, len(timestamps) - 1
        
        while l <= r:
            mid = (l + r) // 2
            time = timestamps[mid][1]

            if time > timestamp:
                r = mid - 1
            else:
                l = mid + 1
                res = timestamps[mid][0]
        
        return res
