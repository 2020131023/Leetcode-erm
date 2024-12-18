class Solution:
    def shortestToChar(self, s, c):
        n = len(s)
        ans = [n] * n
        pre = float("-inf")
        for i, ch in enumerate(s):
            if ch == c:
                pre = i
            ans[i] = min(ans[i], i - pre)
        suf = float("inf")
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                suf = i
            ans[i] = min(ans[i], suf - i)
        return ans