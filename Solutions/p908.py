class Solution:
    def smallestRangeI(self, nums, k):
        mx, mi = max(nums), min(nums)
        return max(0, mx - mi - k * 2)