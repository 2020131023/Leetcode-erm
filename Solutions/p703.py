class KthLargest:
    def __init__(self, k, nums):
        self.q = []
        self.size = k
        for num in nums:
            self.add(num)

    def add(self, val):
        heappush(self.q, val)
        if len(self.q) > self.size:
            heappop(self.q)
        return self.q[0]