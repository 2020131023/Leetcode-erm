class Solution:
    def isSubsequence(self, s, t):
        index = defaultdict(list)
        for i, c in enumerate(t):
            index[c].append(i)
        j = 0
        for c in s:
            if c not in index:
                return False
            pos_list = index[c]
            pos = bisect_left(pos_list, j)
            if pos == len(pos_list):
                return False
            j = pos_list[pos] + 1
        return True