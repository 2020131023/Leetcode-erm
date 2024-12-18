class Solution:
    def nthSuperUglyNumber(self, n, primes):
        q = [1]
        x = 0
        mx_int = (1 << 31) - 1
        for _ in range(n):
            x = heappop(q)
            for k in primes:
                if x <= mx_int // k:
                    heappush(q, k * x)
                if x % k == 0:
                    break
        return x