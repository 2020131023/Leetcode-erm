class Solution:
    def repeatedNTimes(self, nums):
        s = set()
        for x in nums:
            if x in s:
                return x
            s.add(x)