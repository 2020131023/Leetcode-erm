class Solution:
    def escapeGhosts(self, ghosts, target):
        tx, ty = target
        return all(abs(tx - x) + abs(ty - y) > abs(tx) + abs(ty) for x, y in ghosts)