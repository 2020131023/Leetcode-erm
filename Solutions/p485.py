class Solution:
    def findMaxConsecutiveOnes(self, nums):
        return max( len(s) for s in ''.join( str(x) for x in nums ).split('0') )