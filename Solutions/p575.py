class Solution:
    def distributeCandies(self, candyType):
        return min(len(candyType) >> 1, len(set(candyType)))