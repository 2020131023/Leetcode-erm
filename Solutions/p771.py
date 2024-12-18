class Solution:
    def numJewelsInStones(self, jewels, stones):
        s = set(jewels)
        return sum(c in s for c in stones)