class Solution:
    def singleNumber(self, nums):
        a = b = 0
        for c in nums:
            aa = (~a & b & c) | (a & ~b & ~c)
            bb = ~a & (b ^ c)
            a, b = aa, bb
        return b