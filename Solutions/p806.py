class Solution:
    def numberOfLines(self, widths, s):
        last, row = 0, 1
        for c in s:
            w = widths[ord(c) - ord('a')]
            if last + w <= 100:
                last += w
            else:
                row += 1
                last = w
        return [row, last]