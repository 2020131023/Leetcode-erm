class Solution:
    def checkSubarraySum(self, nums, k):
        s = 0
        mp = {0: -1}
        for i, v in enumerate(nums):
            s += v
            r = s % k
            if r in mp and i - mp[r] >= 2:
                return True
            if r not in mp:
                mp[r] = i
        return False