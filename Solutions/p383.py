class Solution:
    def canConstruct(self, ransomNote, magazine):
        cnt = Counter(magazine)
        for c in ransomNote:
            cnt[c] -= 1
            if cnt[c] < 0:
                return False
        return True