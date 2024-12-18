class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        cnt = Counter()
        for i in range(n):
            for j in range(n):
                if img1[i][j]:
                    for h in range(n):
                        for k in range(n):
                            if img2[h][k]:
                                cnt[(i - h, j - k)] += 1
        return max(cnt.values()) if cnt else 0