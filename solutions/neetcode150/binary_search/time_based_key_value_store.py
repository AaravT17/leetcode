class TimeMap:
    def __init__(self):
        self.hashmap = {}  # key = key, value = [(timestamp, value), ...], timestamps are strictly increasing

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append((timestamp, value))
        else:
            self.hashmap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap or self.hashmap[key][0][0] > timestamp:
            return ''

        # the key is in self.hashmap and the earliest timestamp for the key <= the given timestamp
        l, r = 0, len(self.hashmap[key]) - 1
        res = self.hashmap[key][0][1]  # base solution = value with earliest timestamp (since we know it is viable)
        while l <= r:
            m = l + ((r - l) // 2)
            ts = self.hashmap[key][m][0]
            if ts > timestamp:
                # not a viable solution
                r = m - 1
            else:
                # ts <= timestamp => viable solution, and its timestamp > timestamp of res' current value (it is
                # at a greater index in self.hashmap[key] => greater timestamp), set res to this value
                res = self.hashmap[key][m][1]
                l = m + 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
