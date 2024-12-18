class Solution:
    def findTheDifference(self, s, t):
        cnt = Counter(s)
        for c in t:
            cnt[c] -= 1
            if cnt[c] < 0:
                return c