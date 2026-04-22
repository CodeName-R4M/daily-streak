class RecentCounter:

    def __init__(self):
        self.arr = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.arr.append(t)

        while self.arr[self.start] < t - 3000:
            self.start += 1

        return len(self.arr) - self.start